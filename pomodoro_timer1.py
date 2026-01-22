import time 
our_worktime= float(input("write the work hour you want? : "))

if  0 <= our_worktime <= 10:            #girilen saati kontrol ediyoruz
 total_seconds = int(our_worktime * 3600)      #verilen saniye ye çeviriyorum sistem saniye üzerinden diye 
else:
 print(input("Write hour between 0 and 10 numbers: "))

def countdown (seconds):
 while seconds > 0:
  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  secs = seconds % 60
  print(f"{hours:02d}:{minutes:02d}:{secs:02d}" , end="\r")     #sayıları 02:30:55 gibi yazıcak.
  time.sleep(1)
  seconds-= -1

work_minutes = 25
break_minutes = 5
work = work_minutes * 60
break_time= break_minutes * 60
pomodoro_count = total_seconds // (work + break_time)       #break ile beraber kaç pomodoro olucak onu sayıyoruz.

for i in range(pomodoro_count):
 print(f"\n Pomodoro {i+1} started")

 print("WORK TİME")
 countdown(work)

 print("BREAK TİME!")
 countdown(break_time)

print("WELL DONE,YOU WORK VERY HARD NOW!!")
print("YOU DESERVED A GOOD BREAK TİME" \
"SEE YOU SOON")
