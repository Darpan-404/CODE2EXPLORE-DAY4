registerno = input("Enter your Register Number: ")
D = int(registerno[-1])

print("Register Digit (D):", D)

n = int(input("Enter number of activity scores: "))

activity_scores = []
for i in range(n):
    val = int(input("Enter score: "))
    activity_scores = activity_scores + [val]

lrisk = []
mrisk = []
hrisk = []
crisk = []

ignore = 0
valid = 0

for score in activity_scores:

    if score < 0:
        ignore = ignore + 1

    else:
        valid = valid + 1

        if score <= 30:
            lrisk = lrisk + [score]

        elif score <= 60:
            mrisk = mrisk + [score]

        elif score <= 100:
            hrisk = hrisk + [score]

        else:
            crisk = crisk + [score]

rmcount = 0

if D % 2 == 0:
    rmcount = rmcount + len(lrisk)
    lrisk = []

else:
    rmcount = rmcount + len(crisk)
    crisk = []

print("\nAfter Personalized Filtering:")

print("Low Risk:", lrisk)
print("Medium Risk:", mrisk)
print("High Risk:", hrisk)
print("Critical Risk:", crisk)

print("\nTotal Valid Entries:", valid)
print("Ignored Entries:", ignore)
print("Removed Due to Personalization:", rmcount)
