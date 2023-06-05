import random
import csv

# Parameters for good posture
num_samples_good = 5000  # Number of samples for good posture
fsr_min_good = 55000  # Minimum FSR value for good posture
fsr_max_good = 60000  # Maximum FSR value for good posture
ultrasonic_min_good = 5  # Minimum ultrasonic distance for good posture (in cm)
ultrasonic_max_good = 20  # Maximum ultrasonic distance for good posture (in cm)
imu_min_good = -5000  # Minimum IMU value for good posture
imu_max_good = 5000  # Maximum IMU value for good posture

# Parameters for bad posture
num_samples_bad = 5000  # Number of samples for bad posture
fsr_min_bad = 40000  # Minimum FSR value for bad posture
fsr_max_bad = 45000  # Maximum FSR value for bad posture
ultrasonic_min_bad = 25  # Minimum ultrasonic distance for bad posture (in cm)
ultrasonic_max_bad = 50  # Maximum ultrasonic distance for bad posture (in cm)
imu_min_bad = -10000  # Minimum IMU value for bad posture
imu_max_bad = 10000  # Maximum IMU value for bad posture

# Generate sample data for good posture
sample_data_good = []
for _ in range(num_samples_good):
    accel_x = random.randint(-32768, 32767)  # Sample acceleration X
    accel_y = random.randint(-32768, 32767)  # Sample acceleration Y
    fsr_1 = random.randint(fsr_min_good, fsr_max_good)  # Sample FSR 1
    gyro_z = random.randint(-32768, 32767)  # Sample gyro Z
    fsr_3 = random.randint(fsr_min_good, fsr_max_good)  # Sample FSR 3
    fsr_2 = random.randint(fsr_min_good, fsr_max_good)  # Sample FSR 2
    ultrasonic_1 = random.uniform(ultrasonic_min_good, ultrasonic_max_good)  # Sample ultrasonic 1
    ultrasonic_2 = random.uniform(ultrasonic_min_good, ultrasonic_max_good)  # Sample ultrasonic 2
    ultrasonic_3 = random.uniform(ultrasonic_min_good, ultrasonic_max_good)  # Sample ultrasonic 3
    gyro_x = random.randint(imu_min_good, imu_max_good)  # Sample gyro X
    accel_z = random.randint(-32768, 32767)  # Sample acceleration Z
    gyro_y = random.randint(imu_min_good, imu_max_good)  # Sample gyro Y
    ultrasonic_4 = random.uniform(ultrasonic_min_good, ultrasonic_max_good)  # Sample ultrasonic 4

    sample_data_good.append([accel_x, accel_y, fsr_1, gyro_z, fsr_3, fsr_2, ultrasonic_1, ultrasonic_2,
                             ultrasonic_3, gyro_x, accel_z, gyro_y, ultrasonic_4])

# Generate sample data for bad posture
sample_data_bad = []
for _ in range(num_samples_bad):
    accel_x = random.randint(-32768, 32767)  # Sample acceleration X
    accel_y = random.randint(-32768, 32767)  # Sample acceleration Y
    fsr_1 = random.randint(fsr_min_bad, fsr_max_bad)  # Sample FSR 1
    gyro_z = random.randint(-32768, 32767)  # Sample gyro Z
    fsr_3 = random.randint(fsr_min_bad, fsr_max_bad)  # Sample FSR 3
    fsr_2 = random.randint(fsr_min_bad, fsr_max_bad)  # Sample FSR 2
    ultrasonic_1 = random.uniform(ultrasonic_min_bad, ultrasonic_max_bad)  # Sample ultrasonic 1
    ultrasonic_2 = random.uniform(ultrasonic_min_bad, ultrasonic_max_bad)  # Sample ultrasonic 2
    ultrasonic_3 = random.uniform(ultrasonic_min_bad, ultrasonic_max_bad)  # Sample ultrasonic 3
    gyro_x = random.randint(imu_min_bad, imu_max_bad)  # Sample gyro X
    accel_z = random.randint(-32768, 32767)  # Sample acceleration Z
    gyro_y = random.randint(imu_min_bad, imu_max_bad)  # Sample gyro Y
    ultrasonic_4 = random.uniform(ultrasonic_min_bad, ultrasonic_max_bad)  # Sample ultrasonic 4

    sample_data_bad.append([accel_x, accel_y, fsr_1, gyro_z, fsr_3, fsr_2, ultrasonic_1, ultrasonic_2,
                            ultrasonic_3, gyro_x, accel_z, gyro_y, ultrasonic_4])

# Write sample data for good posture to CSV file
header = ['accel_x', 'accel_y', 'fsr_1', 'gyro_z', 'fsr_3', 'fsr_2', 'ultrasonic_1', 'ultrasonic_2',
          'ultrasonic_3', 'gyro_x', 'accel_z', 'gyro_y', 'ultrasonic_4']

filename_good = 'sample_data_good.csv'
with open(filename_good, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(sample_data_good)

print(f"Sample data for good posture generated and saved to {filename_good}")

# Write sample data for bad posture to CSV file
filename_bad = 'sample_data_bad.csv'
with open(filename_bad, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(sample_data_bad)

print(f"Sample data for bad posture generated and saved to {filename_bad}")
