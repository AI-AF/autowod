# autowod
Programatically generate personalized WODs. The goal is to semi-automatically generate WODs the follow the CrossFit level 1 template by randomly picking from a library of exercises. Then score the actual WOD performed along two dimensions: Modality & Movement Category. Use scores from the last `n` days to constrain future WOD generation with the objective of maximizing coverage of the 12-D space of modality and movement category.

Modality
-------------------
## M1. Gymnastics / AthCon
Air Squat, Pull-up, Push-up
Dip. Handstand Push-up, Back Extension 
Sit-up, Jump Lunge, GHD sit up, Nordic HC
Deck & pistol squats ...

## M2. Metabolic Conditioning / MetCon
Run, Bike, Row, Jump Rope ...

## M3. Weightlifting
Deadlift, Cleans, Press, Snatch
Clean and Jerk, Medicine-Ball Drills 
Kettlebell Swing, turkish get ups...

Movement Category
------------------------
- BHD. Bilateral Hip Dominant (e.g. RDL, trap-bar deadlift, barbell deadlift)
- BQD. Bilateral Quad Dominant (e.g. goblet squat, front squat, back squat)MC
- UHD. Unilateral Hip Dominant (e.g. reverse lunge, single-leg RDL)
- UQD. Unilateral Quad Dominant (e.g. split squat, forward lunge)MC
- BPS. Bilateral Upper-Body Push (e.g. push-up, bench press)
- BPL. Bilateral Upper-Body Pull (e.g. chin-up, inverted row)MC
- UPS. Unilateral Upper-Body Push (e.g. single-arm landmine press, single-arm overhead press)
- UPL. Unilateral Upper-Body Pull (e.g. single-arm row, single-arm lat pull down)MC
- COR. Core (e.g. plank, ab wheel rollout, farmer’s walk)


