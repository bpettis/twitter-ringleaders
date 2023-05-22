from datetime import datetime





if __name__ == "__main__":
    start_time = datetime.now()
    print(f'FYI: Script started directly as __main__ at {start_time}')
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f'Finished at {end_time}')
    print(f'Total execution was: {total_time}')