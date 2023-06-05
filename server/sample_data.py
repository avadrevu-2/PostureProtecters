import random
import csv


def generate_sample_data(filename, num_samples_good, num_samples_bad):
    fieldnames = [
        "accel_x", "accel_y", "fsr_1", "gyro_z", "fsr_3", "fsr_2",
        "ultrasonic_1", "ultrasonic_2", "ultrasonic_3",
        "gyro_x", "accel_z", "gyro_y", "ultrasonic_4"
    ]

    fsr_min_good = 58000
    fsr_max_good = 60000
    ultrasonic_min_good = 10
    ultrasonic_max_good = 20
    imu_min_good = -2000
    imu_max_good = 2000

    fsr_min_bad = 40000
    fsr_max_bad = 42000
    ultrasonic_min_bad = 40
    ultrasonic_max_bad = 50
    imu_min_bad = -4000
    imu_max_bad = 4000

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # Generate good posture samples
        for _ in range(num_samples_good):
            data = {
                "accel_x": random.randint(imu_min_good, imu_max_good),
                "accel_y": random.randint(imu_min_good, imu_max_good),
                "fsr_1": random.randint(fsr_min_good, fsr_max_good),
                "gyro_z": random.randint(imu_min_good, imu_max_good),
                "fsr_3": random.randint(fsr_min_good, fsr_max_good),
                "fsr_2": random.randint(fsr_min_good, fsr_max_good),
                "ultrasonic_1": random.uniform(ultrasonic_min_good, ultrasonic_max_good),
                "ultrasonic_2": random.uniform(ultrasonic_min_good, ultrasonic_max_good),
                "ultrasonic_3": random.uniform(ultrasonic_min_good, ultrasonic_max_good),
                "gyro_x": random.randint(imu_min_good, imu_max_good),
                "accel_z": random.randint(imu_min_good, imu_max_good),
                "gyro_y": random.randint(imu_min_good, imu_max_good),
                "ultrasonic_4": random.uniform(ultrasonic_min_good, ultrasonic_max_good)
            }
            writer.writerow(data)

        # Generate bad posture samples
        for _ in range(num_samples_bad):
            data = {
                "accel_x": random.randint(imu_min_bad, imu_max_bad),
                "accel_y": random.randint(imu_min_bad, imu_max_bad),
                "fsr_1": random.randint(fsr_min_bad, fsr_max_bad),
                "gyro_z": random.randint(imu_min_bad, imu_max_bad),
                "fsr_3": random.randint(fsr_min_bad, fsr_max_bad),
                "fsr_2": random.randint(fsr_min_bad, fsr_max_bad),
                "ultrasonic_1": random.uniform(ultrasonic_min_bad, ultrasonic_max_bad),
                "ultrasonic_2": random.uniform(ultrasonic_min_bad, ultrasonic_max_bad),
                "ultrasonic_3": random.uniform(ultrasonic_min_bad, ultrasonic_max_bad),
                "gyro_x": random.randint(imu_min_bad, imu_max_bad),
                "accel_z": random.randint(imu_min_bad, imu_max_bad),
                "gyro_y": random.randint(imu_min_bad, imu_max_bad),
                "ultrasonic_4": random.uniform(ultrasonic_min_bad, ultrasonic_max_bad)
            }
            writer.writerow(data)

        # Mix some samples between good and bad posture
        for _ in range(100):
            data = {
                "accel_x": random.randint(imu_min_good, imu_max_good),
                "accel_y": random.randint(imu_min_good, imu_max_good),
                "fsr_1": random.randint(fsr_min_bad, fsr_max_bad),
                "gyro_z": random.randint(imu_min_good, imu_max_good),
                "fsr_3": random.randint(fsr_min_bad, fsr_max_bad),
                "fsr_2": random.randint(fsr_min_bad, fsr_max_bad),
                "ultrasonic_1": random.uniform(ultrasonic_min_bad, ultrasonic_max_bad),
                "ultrasonic_2": random.uniform(ultrasonic_min_bad, ultrasonic_max_bad),
                "ultrasonic_3": random.uniform(ultrasonic_min_bad, ultrasonic_max_bad),
                "gyro_x": random.randint(imu_min_good, imu_max_good),
                "accel_z": random.randint(imu_min_good, imu_max_good),
                "gyro_y": random.randint(imu_min_good, imu_max_good),
                "ultrasonic_4": random.uniform(ultrasonic_min_good, ultrasonic_max_good)
            }
            writer.writerow(data)

    print("Sample data generation completed.")


generate_sample_data('sample_data_good.csv', 5000, 100)
generate_sample_data('sample_data_bad.csv', 100, 5000)

