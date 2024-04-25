import cricket_module as cm
for i in range:
    i.update({"name":input("name of cricketer:-")})
    print(i)
print("name of cricketer:",cm.cricket["name"])
print("nno of matches palyed by cricketer:",cm.cricket["matchs"],"matches")
print("no of balls played:",cm.cricket["balls faced"],"balls")
print("no of runs:",cm.cricket["runs"],"runs")
print("no of not out matches:",cm.cricket["not outs"],"matches")
print("no of no balles faced:",cm.cricket["no balls faced"],"balls")
strick_rate=(cm.cricket["runs"]/cm.cricket["balls faced"])/100
avg=cm.cricket["runs"]/(cm.cricket["matchs"]-cm.cricket["not outs"])
print("strick rate of ",cm.cricket["name"]," is ",strick_rate)
print("the avg score of ",cm.cricket["name"],"is",avg)
import statistics
cricketers = [
    {"name": "Virat", "ODIs": 50, "runs": 2000, "4s": 250, "6s": 50, "balls_faced": 1800, "wickets": 10},
    {"name": "Rohit", "ODIs": 40, "runs": 1800, "4s": 200, "6s": 40, "balls_faced": 1600, "wickets": 5},
]
r_list = [player["runs"] for player in cricketers]
balls_faced_list = [player["balls_faced"] for player in cricketers]
wickets_list = [player["wickets"] if "wickets" in player else 0 for player in cricketers]

# Calculate averages using built-in statistics module
avg_runs = statistics.mean(r_list)
average_balls_faced = statistics.mean(balls_faced_list) 
average_wickets = statistics.mean(wickets_list)

print("Average runs : ",avg_runs)
print("Average balls faced : ",average_balls_faced)
print("Average wickets : ",average_wickets)

for player in cricketers:
    strike_rate = (player["runs"] / player["balls_faced"]) * 100
    print(f"{player['name']} - Strike Rate: {strike_rate:.2f}")
