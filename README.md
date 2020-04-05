# AutoWOD
Programatically generate personalized WODs. The goal is to semi-automatically generate WODs the follow the CrossFit level 1 template by randomly picking from a library of exercises. Then score the actual WOD performed along two dimensions: Modality & Movement Category. Use scores from the last `n` days to constrain future WOD generation with the objective of maximizing coverage of the 12-D space of modality and movement category.

Modality
-------------------
- **G**. Gymnastics / AthCon: Air Squat, Pull-up, Push-up, Dip. Handstand Push-up, Back Extension, Sit-up, Jump Lunge, GHD sit up, Nordic HC, Deck & pistol squats etc.
- **M**. Metabolic Conditioning / MetCon: Run, Bike, Row, Jump Rope etc.
- **W**. Weightlifting: e.g. Deadlift, Cleans, Press, Snatch Clean and Jerk, Medicine-Ball Drills, Kettlebell Swing, turkish get ups etc.

Movement Category
------------------------
- **BHD**. Bilateral Hip Dominant (e.g. RDL, trap-bar deadlift, barbell deadlift)
- **BQD**. Bilateral Quad Dominant (e.g. goblet squat, front squat, back squat)
- **UHD**. Unilateral Hip Dominant (e.g. reverse lunge, single-leg RDL)
- **UQD**. Unilateral Quad Dominant (e.g. split squat, forward lunge)
- **BPS**. Bilateral Upper-Body Push (e.g. push-up, bench press)
- **BPL**. Bilateral Upper-Body Pull (e.g. chin-up, inverted row)
- **UPS**. Unilateral Upper-Body Push (e.g. single-arm landmine press, single-arm overhead press)
- **UPL**. Unilateral Upper-Body Pull (e.g. single-arm row, single-arm lat pull down)
- **COR**. Core (e.g. plank, ab wheel rollout, farmer’s walk)

Format
------------------------
- **BroScience**: Lift heavy, learn skills, rest long 
- **Task priority**: Scored for time - Benchmark workouts, 12 days of Christmas etc.
- **Time priority**: Scored for reps - AMRAP of triplet moves in fixed time, Scored tabata or other work rest ratio etc.
- **Form priority**: Not scored - EMOM, alternating sets with target reps etc. 


