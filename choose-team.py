import argparse
import random

def get_team_members(f = "team-list"):
    members = {}
    with open(f) as team:
        for member in team:
            if member.startswith("#"):
                continue
            name, num = member.split(",")
            members[name.strip()] = int(num)
    return members

def choose_team(members):
    chosen = []
    for i in range(5):
        applicable = [x for x in members.items() if x[1] <= min(members.values()) and x[0] not in chosen]
        member, count = random.choice(applicable)
        chosen.append(member)
        members[member] += 1
    return chosen

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("matches", type=int, help="Number of matches to play")
    config = parser.parse_args()
    team = get_team_members()
    for i in range(config.matches):
        t = choose_team(team)
        print(f"==== Team for match {i + 1}:")
        for m in t:
            print(m)
