pool_volume = int(input())
pipe_1_flow = int(input())
pipe_2_flow = int(input())
hours = float(input())

pipe_1_result = pipe_1_flow * hours
pipe_2_result = pipe_2_flow * hours

total_result = pipe_1_result + pipe_2_result

if total_result <= pool_volume:
    pool_fullness = total_result / pool_volume
    pipe_1_percent = pipe_1_result / total_result
    pipe_2_percent = pipe_2_result / total_result

    print(f"The pool is {pool_fullness :.2%} full. "
          f"Pipe 1: {pipe_1_percent :.2%}. "
          f"Pipe 2: {pipe_2_percent :.2%}.")
else:
    print(f"For {hours} hours the pool overflows with {total_result - pool_volume :.2f} liters.")
