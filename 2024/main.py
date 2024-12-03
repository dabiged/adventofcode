from collections import defaultdict
days_done = defaultdict(bool)

for day in range(1,26):
    day='day'+str(day).zfill(2)
    for part in range(1,3):
        if day != 'day25' and part != '_02':
            part='_'+str(part).zfill(2)
            try:
                days_done[day+part]=getattr(__import__(day,fromlist=[day+part]), day+part)
            except Exception as Err:
                pass

if __name__ == "__main__":
    for func in days_done.values():
        func()
