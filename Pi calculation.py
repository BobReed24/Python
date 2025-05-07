from mpmath import mp
import psutil
import os
import time

def get_system_usage():
    """
    Returns the current CPU and RAM usage percentages.
    """
    cpu_usage = psutil.cpu_percent(interval=0)  
    ram_usage = psutil.virtual_memory().percent  
    return cpu_usage, ram_usage

def calculate_pi_to_file(file_path, digits, chunk_size=100000): # Default chunk size is 100,000 
    """
    Incrementally calculate pi to a specified number of digits and write to a file.

    :param file_path: Path to the file where the result will be stored.
    :param digits: Total number of digits to calculate.
    :param chunk_size: Number of digits to calculate per step.
    """

    mp.dps = chunk_size  

    start_time = time.time()

    with open(file_path, 'w') as file:

        file.write("3.")
        print('Added "3." to the beginning of the file.')

    with open(file_path, 'a+') as file:
        total_written = 0

        while total_written < digits:

            remaining_digits = min(chunk_size, digits - total_written)
            mp.dps = total_written + remaining_digits

            pi_value = str(mp.pi)[total_written + 2:total_written + 2 + remaining_digits]  

            file.write(pi_value)
            total_written += remaining_digits

            cpu_usage, ram_usage = get_system_usage()

            print(f"Written {total_written}/{digits} digits to file... | CPU Usage: {cpu_usage}% | RAM Usage: {ram_usage}%")

    end_time = time.time()
    total_time = end_time - start_time
    minutes = total_time // 60
    seconds = total_time % 60

    print(f"Calculation complete. {digits} digits written to {file_path} in {int(minutes)} minutes {int(seconds)} seconds.")

output_file = "pi_digits.txt"
# Total digits to print
total_digits = float('inf') # Default is infinity 
calculate_pi_to_file(output_file, total_digits)
