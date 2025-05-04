class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit

def compare(job):
    return -job.profit  # for descending order

def job_scheduling(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=compare)

    # Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Initialize time slots and result array
    slot = [False] * (max_deadline + 1)
    result = [' '] * (max_deadline + 1)

    total_profit = 0
    count = 0

    # Schedule jobs
    for job in jobs:
        for j in range(job.deadline, 0, -1):
            if not slot[j]:
                slot[j] = True
                result[j] = job.id
                total_profit += job.profit
                count += 1
                break

    # Print result
    print("Scheduled Jobs:", end=" ")
    for i in range(1, max_deadline + 1):
        if slot[i]:
            print(result[i], end=" ")
    print(f"\nTotal Profit: {total_profit}")

def main():
    n = int(input("Enter number of jobs: "))
    jobs = []

    print("Enter job id, deadline, and profit:")
    for _ in range(n):
        parts = input().split()
        job_id = parts[0]
        deadline = int(parts[1])
        profit = int(parts[2])
        jobs.append(Job(job_id, deadline, profit))

    job_scheduling(jobs)

if __name__ == "__main__":
    main()
