def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    steering_angle = params['steering_angle']
    progress = params['progress']
    steps = params['steps']
    is_offtrack = not all_wheels_on_track

    # Set the default reward
    reward = 1.0

    # Add rewards and penalties based on different conditions
    # Reward the agent for staying on the track and making progress
    if not is_offtrack and all_wheels_on_track:
        reward += 0.5 * speed * progress

        # Additional reward for being close to the center of the track
        reward += 0.1 * (track_width - distance_from_center)

        if abs(steering_angle) > 15 and speed > 2.0:
            reward += 2.0

    # Add a penalty for taking sharp turns to avoid zig-zagging behavior
    reward -= 0.2 * abs(steering_angle)

    # Add a penalty for slow progress to encourage faster completion
    reward -= 0.2 * (1.0 - progress)

    # Additional penalty and recovery reward for drifting outside the track
    if is_offtrack:
        reward -= 2.0  # A penalty for drifting outside the track
        if abs(steering_angle) > 15 and speed > 2.0:
            reward += 1.0

            if steering_angle < 0:
                reward += 2.0

            elif steering_angle > 0:
                reward += 2.0

    if progress == 100:
        reward += 10.0

    return float(reward)
