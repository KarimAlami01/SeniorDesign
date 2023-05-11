teams = {
    "Atlanta Hustle": "/static/teams/hustle.png",
    "Austin Sol": "/static/teams/sol.png",
    "Boston Glory": "/static/teams/glory.png",
    "Carolina Flyers": "/static/teams/flyers.png",
    "Chicago Union": "/static/teams/union.png",
    "Colorado Summit": "/static/teams/summit.png",
    "Dallas Legion": "/static/teams/legion.png",
    "DC Breeze": "/static/teams/breeze.png",
    "Detroit Mechanix": "/static/teams/mechanix.png",
    "Houston Havoc": "/static/teams/havoc.png",
    "Indianapolis AlleyCats": "/static/teams/cats.png",
    "Los Angeles Aviators": "/static/teams/aviators.png",
    "Madison Radicals": "/static/teams/radicals.png",
    "Minnesota Wind Chill": "/static/teams/windchill.png",
    "Montreal Royal": "/static/teams/royal.png",
    "New York Empire": "/static/teams/empire.png",
    "Oakland Spiders": "/static/teams/spiders.png",
    "Philadelphia Phoenix": "/static/teams/phoenix.png",
    "Pittsburgh Thunderbirds": "/static/teams/thunderbirds.png",
    "Portland Nitro": "/static/teams/nitro.png",
    "Salt Lake Shred": "/static/teams/shred.png",
    "San Diego Growlers": "/static/teams/growlers.png",
    "Seattle Cascades": "/static/teams/cascades.png",
    "Toronto Rush": "/static/teams/rush.png",
    "Not Real": "https://via.placeholder.com/300x300.png?text=Image"
}

import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        team = request.form["team"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(team),
            temperature=0.6,
            max_tokens=4040,  # increase max tokens to get longer output
            n=3,  
            stop=None,  # no stop sequence
        )
        result = ""
        for choice in response.choices:
            result += choice.text
        return redirect(url_for("report", result=result, team = team))

    result = request.args.get("result")
    return render_template("index.html")


def generate_prompt(team):
    return f"Here is a team in the AUDL. Generate a well-structured 2 paragraph sports article giving a brief description about the {team} and predicting how their upcoming 2023 season will go."

@app.route("/report")
def report():
    result = request.args.get("result")
    team = request.args.get('team')

    team_logo_url = None
    if team in teams:
        team_logo_url = teams[team]
    return render_template("report.html", result=result, team=team, team_logo_url=team_logo_url)

@app.route("/match1")
def match1():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Can you be a sports reporter and write a three paragraph article with a title about this game that occured in the 2023 season of the AUDL? Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1	Q2	Q3	Q4	T Toronto Rush	1	5	2	3	11 New York Empire	5	6	6	7	24 Team Stats Toronto Rush	New York Empire Completions	90% (234/260)	94% (231/246) Hucks	50% (5/10)	57% (8/14) Hold %	40% (10/25)	92% (12/13) O-Line Conversion %	29% (10/34)	67% (12/18) Break %	8% (1/13)	48% (12/25) D-Line Conversion %	17% (1/6)	57% (12/21) Red Zone Conversion %	78% (7/9)	88% (15/17) Blocks	9	16 Turnovers	26	15 Strong Empire Between Friday and Saturday, Toronto failed to win a single quarter against the Empire and the Glory. On Friday night in New Rochelle, the two teams were tied 1-1 through six sloppy minutes in the opening period, but New York outscored Toronto 7-2 over the next 12 minutes to create more than enough separation. The Rush’s only break came with 4:23 left in the second to bring Toronto back within three, but another 6-1 spurt from the Empire left the Rush in the dust. “Toronto made it easy for us in many ways, giving us the disc without having to work that hard for it,” said New York’s Ben Jagt. “We were 12-for-21 on break chances, so a little sloppier than we’d like as far as D-line offense. We’ll definitely be looking to clean that up this weekend.” Despite their desire to be even more efficient, the Empire’s D-line has converted 23 breaks in 43 chances (53.3 percent) across their first two games of the season. “Going up against the best offense in the league every week [at practice] helps, and having to cover Jack [Williams] at practice makes it feel like a relief to get to the games and have anyone else to cover,” said New York’s Ryan Drost. After two lopsided home wins, the Empire now carry a 17-game winning streak into Saturday’s trip to DC, the city where New York last lost.",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match1.html", result=result)

@app.route("/match2")
def match2():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Can you be a sports reporter and write a three paragraph article with a title about this game that occured in the 2023 season of the AUDL? Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1 Q2 Q3 Q4 T Carolina Flyers 4 4 6 5 19 Atlanta Hustle 4 7 5 8 24 Team Stats Carolina Flyers Atlanta Hustle Completions 92% (220/238) 95% (219/231) Hucks 75% (12/16) 77% (10/13) Hold % 68% (17/25) 81% (17/21) O-Line Conversion % 57% (17/30) 65% (17/26) Break % 10% (2/21) 24% (6/25) D-Line Conversion % 29% (2/7) 55% (6/11) Red Zone Conversion % 69% (11/16) 88% (15/17) Blocks 0 9 Turnovers 18 12 The Hustle are one such team that should be feeling greedy right now, determined to bank as many early victories as possible. Before the season began, Head Coach Tuba Benson-Jaja examined the Hustle’s schedule, saw three straight home games against Indianapolis, Carolina, and Austin, and immediately felt that his team had to be at least 2-1 before hitting the road in Week 4. After impressive back-to-back wins against the AlleyCats and Flyers, the Hustle have set a solid foundation. But a win over the Sol on Friday would cement Atlanta’s status as a true title contender. “We have so much more growth to do,” said Benson-Jaja. “They know it and have been holding each other accountable in many ways since Friday’s game.” Against the Flyers, Atlanta led virtually wire-to-wire, but still struggled to put Carolina away until the late stages of the game. They were only broken twice in four quarters, but one of those breaks came midway through the fourth and inched the Flyers within one. Leading 19-18 with six-plus minutes left, Atlanta scored five of the last six goals to finish the job with a flurry, much like DC did against Carolina the previous week, as the Hustle prevailed 24-19. “I was very impressed with how efficient and methodical the Atlanta offense was at possessing the disc,” said Flyers Coach Mike DeNardis. “We had them in several tight spots, but they almost always found a way to exploit a small crack in our defense.” Through two games, Atlanta’s averaging just 9.5 turnovers per contest. No other team in the league has had a single-digit turnover game yet this season. “Part of the push for this win was to get the mental hurdle off our backs,” said Benson-Jaja. “Many of the players that joined the franchise last year had never beaten the Flyers. So this was an important game for us in that regard. I needed them to see that it was possible.” Hustle big man Brett Hulsmeyer continued his tremendous start with four assists, two goals, one block, and a team-high 598 total yards. He also played an astonishing 31 points, eight more than anyone else on Atlanta. Rookie Liam Haberfield enjoyed a breakout game too, tallying five assists, three goals, and 522 total yards. Jacob Fairfax produced a game-high 690 total yards and dished five assists for the short-handed Flyers, who dipped to 0-2 for the second time in three seasons. Of course, the last time Carolina started 0-2, the Flyers rallied to win the AUDL Championship. Both the Hustle and Flyers host Austin this weekend, with Atlanta aiming for 3-0 and Carolina yearning to avoid 0-3, though Carolina has the benefit of getting the Sol on Saturday in the second day of the back-to-back.",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match2.html", result=result)

@app.route("/match3")
def match3():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Can you be a sports reporter and write a three paragraph article with a title about this game that occured in the 2023 season of the AUDL? Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1 Q2 Q3 Q4 T Colorado Summit 8 3 6 6 23 San Diego Growlers 3 5 5 3 16 Team Stats Colorado Summit San Diego Growlers Completions 94% (268/284) 91% (245/270) Hucks 64% (9/14) 100% (8/8) Hold % 67% (12/18) 52% (13/25) O-Line Conversion % 60% (12/20) 37% (13/35) Break % 44% (11/25) 17% (3/18) D-Line Conversion % 52% (11/21) 50% (3/6) Red Zone Conversion % 85% (17/20) 71% (10/14) Blocks 14 7 Turnovers 16 25 The San Diego Growlers hosted the defending AUDL West Division Colorado Summit on Friday, May 5 at Mira Mesa HS for their 2023 season opener. San Diego started hot on defense when a sprinting Reggie Sung laid out for the block, then Max Hume dished to Jan Szmanda for the immediate break score. Colorado quickly equalized, then rattled off three breaks in a row after some uncharacteristic Growlers turnovers. After another miscue, Paul Lally came up with a huge block to negate a score but injured his knee on the play and would not return. San Diego eventually held when Trevor Purdy connected with Tyler Bacon. Both teams traded goals, then the Summit scored three straight to close the quarter up 8-3. Colorado continued their 1st quarter momentum with a break after both teams added a few turnovers, but Max Hume responded with a great backhand huck to Stefan Samu, 9-4. The teams traded scores, then the Growlers found some life with two consecutive break scores to reduce the deficit to 10-7. The Summit held on offense and after a couple turnovers, Samu lofted the disc to Hume who went up big for the skying catch over his defender, 11-8. The Summit scored two in a row to start the third quarter, but the Growlers bounced back with a Travis Dunn assist to Jordan Queckboerner. The two teams traded goals for the rest of the quarter, as Colorado extended its lead to 17-13. The Growlers led off the final frame with another turnover which the Summit cashed in for the break, but Elliot Warner's lefty flick to Hume got the pack back on track. Colorado took firm control of the game with a hold then several breaks in a row to pull away from the Growlers. Travis Dunn found Bacon for a score, but too late, as the Summit came out on top 23-16. The Growlers were led by Max Hume with a +4 performance (2 assists, 2 goals), while Travis Dunn (4 assists, 2 goals, 3 turnovers) and Elliot Warner (3 assists, 1 goal, 1 block, 2 turnovers) each contributed +3 games, respectively. San Diego will need to recover quickly as they host the Portland Nitro on Saturday, May 13 at Mission Bay HS.",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match3.html", result=result)

@app.route("/match4")
def match4():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Can you be a sports reporter and write a three paragraph article with a title about this game that occured in the 2023 season of the AUDL? Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1 Q2 Q3 Q4 T Salt Lake Shred 3 6 8 5 22 Portland Nitro 8 5 5 2 20 Team Stats Salt Lake Shred Portland Nitro Completions 95% (250/263) 94% (250/267) Hucks 57% (4/7) 64% (7/11) Hold % 75% (15/20) 63% (15/24) O-Line Conversion % 68% (15/22) 52% (15/29) Break % 26% (6/23) 23% (5/22) D-Line Conversion % 50% (6/12) 63% (5/8) Red Zone Conversion % 100% (10/10) 81% (13/16) Blocks 5 5 Turnovers 13 17 The reigning top two in the West certainly looked like the division’s standard bearing duo again this past weekend, as Colorado and Salt Lake both swept through their doubleheader road trips with two wins apiece. The Summit led by as many as seven in both of their SoCal contests, ultimately prevailing by a combined 10 goals—seven and three, respectively—against the San Diego Growlers and Los Angeles Aviators, while the Shred required an epic comeback on Friday against Portland prior to their second shredding of Seattle in as many weeks. “We weren’t prepared for Nitro’s intensity,” said Salt Lake’s Sean Connole, trying to explain the Shred’s slow start that had them down 8-3 after 12 minutes in Portland. “I think many of us were still distracted by Utah Wild’s crushing loss to Oregon in overtime [in the preceding Western Ultimate League game at the same stadium]. We weren’t expecting force middle. We had some chemistry and connection issues. Portland wasn’t phased and was feeding off the energy.” The Nitro still led by four with less than three minutes remaining in the third, but Portland’s offense faltered as the Shred made a critical 7-1 run, transforming an 17-13 deficit into a 20-18 lead with less than four minutes to play. Salt Lake’s O-line did the rest, completing one careful pass after another in the closing moments to seal the deal, never again providing Portland with the shot at an equalizer. “We put the D-line in a position that they hadn’t experienced much last season, and they rose to the challenge to chip away at the lead each quarter,” said Connole. A super satisfying road result for Salt Lake doubled as a demoralizing home defeat for Portland, the Nitro’s 10th consecutive loss since starting last year 2-1. Portland travels to Los Angeles and San Diego this coming weekend, with all three teams desperate for their first wins of the year.",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match4.html", result=result)

@app.route("/match5")
def match5():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Can you be a sports reporter and write a three paragraph article with a title about this game that occured in the 2023 season of the AUDL? Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1 Q2 Q3 Q4 T Toronto Rush 4 2 5 3 14 Boston Glory 5 8 7 5 25 Team Stats Toronto Rush Boston Glory Completions 90% (276/306) 92% (217/236) Hucks 56% (5/9) 58% (7/12) Hold % 50% (13/26) 87% (13/15) O-Line Conversion % 38% (13/34) 54% (13/24) Break % 7% (1/15) 42% (11/26) D-Line Conversion % 9% (1/11) 55% (11/20) Red Zone Conversion % 71% (10/14) 89% (16/18) Blocks 10 17 Turnovers 30 19 Boston loves openers I’m wary about getting too optimistic regarding the Boston Glory, who are now 3-0 in season openers but 7-15 in all other games, but Saturday’s steamrolling over the Toronto Rush was as decisive a result as the third-year franchise has ever had. It came, admittedly, against a fatigued Toronto team that was outscored 49-25 this past weekend, however the Glory are hoping they establish a more consistent product in 2023. “Confidence is high, but we are treading lightly,” said Boston’s Brendan McCann. “Philly is going to be a great measure of where we stand.” McCann and Chris Bartoli both finished plus-eight playing D-line against the Rush, with Bartoli creating five of Boston’s 17 blocks, the most the Glory have ever had in a single game. Offensively, Boston was only broken once, though the Rush had 10 other break chances that they couldn’t cash in on. Ben Sadok produced 589 yards of offense, nearly 200 more than anyone else in the game, along with three assists. “We have a much higher ceiling that years past,” said McCann.",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match5.html", result=result)

@app.route("/match6")
def match6():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Can you be a sports reporter and write a three paragraph article with a title about this game that occured in the 2023 season of the AUDL? Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1 Q2 Q3 Q4 T Salt Lake Shred 7 9 4 5 25 Seattle Cascades 3 5 4 7 19 Team Stats Salt Lake Shred Seattle Cascades Completions 96% (259/270) 94% (290/310) Hucks 67% (6/9) 100% (4/4) Hold % 67% (12/18) 52% (14/27) O-Line Conversion % 57% (12/21) 47% (14/30) Break % 48% (13/27) 28% (5/18) D-Line Conversion % 81% (13/16) 63% (5/8) Red Zone Conversion % 100% (18/18) 78% (14/18) Blocks 9 7 Turnovers 11 20 Individual Leaders Salt Lake Shred Seattle Cascades Assists 4 - E L'Heureux 5 - G Martin Goals 7 - J Duennebeil 4 - J Brown Blocks 2 - K Weinberg 1 - Seven players Completions 32 - L Yorgason 51 - M Munoz Points Played 22 - E L'Heureux 26 - K El-Salaam Plus/Minus 7 - J Duennebeil; J Miller 7 - Z Raunig Team Stats Salt Lake Shred Seattle Cascades Completions 96% (259/270) 94% (290/310) Hucks 67% (6/9) 100% (4/4) Hold % 67% (12/18) 52% (14/27) O-Line Conversion % 57% (12/21) 47% (14/30) Break % 48% (13/27) 28% (5/18) D-Line Conversion % 81% (13/16) 63% (5/8) Red Zone Conversion % 100% (18/18) 78% (14/18) Blocks 9 7 Turnovers 11 20",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match6.html", result=result)

@app.route("/match7")
def match7():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Can you be a sports reporter and write a three paragraph article with a title about this game that occured in the 2023 season of the AUDL? Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1 Q2 Q3 Q4 T Minnesota Wind Chill 5 6 5 7 23 Indianapolis AlleyCats 8 4 5 4 21 Team Stats Minnesota Wind Chill Indianapolis AlleyCats Completions 96% (273/283) 96% (287/299) Hucks 77% (10/13) 100% (11/11) Hold % 73% (16/22) 68% (17/25) O-Line Conversion % 67% (16/24) 61% (17/28) Break % 28% (7/25) 18% (4/22) D-Line Conversion % 70% (7/10) 67% (4/6) Red Zone Conversion % 76% (13/17) 80% (12/15) Blocks 10 5 Turnovers 10 12 The Indianapolis AlleyCats returned home from their humbling Week 1 loss in Atlanta, determined to rediscover the taste of victory. But after quickly bolting to a 4-0 lead against Minnesota, the Wind Chill stormed back and spoiled Indy’s home opener with a thrilling 23-21 win, sending the AlleyCats spiraling to 0-2 with a tricky trip to Chicago on tap next. “That was a helluva game and a satisfying result to start the season,” said Wind Chill veteran Josh Klane. “Clearly there was rust and some nerves to kick off the season, especially considering we were playing a strong squad who have been playing together forever. Additionally, we knew this game was going to have a big impact down the road, so I think we simply just needed a few points to settle down and get into a rhythm.” Broken on their first three O-points of the game, the Wind Chill finally stabilized and were broken just once more the rest of the day. Minnesota finished with only 10 turnovers over the four quarters and converted seven of their 10 break opportunities in the clutch. “I don’t feel as if there was one moment that shifted the tide, rather after the first four points of the game our offense was incredibly clean and made few mistakes despite the pressure and height of the Indianapolis defense,” said Minnesota’s Dylan DeClerck. DeClerck and Tanner Barcus each registered three blocks on the Wind Chill D-line, while Marco Dregni was widely praised for his contributions on offense, finishing with five goals, two assists, and 445 receiving yards. Indy veterans Keegan North, Rick Gross, and Cameron Brock all accumulated significant yards and numerous scores, but each had multiple throwaways, which left the AlleyCats certifiably frustrated in the aftermath. “We will lose every game until we decide to play pro ultimate instead of college ultimate,” said Brock. “We’re losing games between the ears. I can deal with being physically outmatched, but we’re just playing backyard ultimate, and nothing is worse than losing in a way that’s so controllable.” The AlleyCats, one of the two remaining AUDL franchises from the league’s inaugural 2012 season, have never before started 0-3, and they’ll have to win at Chicago, something they haven’t done since 2018, to avoid further frustration. Minnesota gets to bask in the glory of the comeback victory for another 11 days before hosting Pittsburgh on May 20. “With championship aspirations, all we are focused on is getting better each week, and we’re looking forward to continuing to build as we head towards our home opener,” said Klane.",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match7.html", result=result)

@app.route("/match8")
def match8():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You are a reputable sports reporter for the 2023 season of the AUDL, write a well-structured three paragraph article with a title about this matchup between the Dallas Legion and the Austin Sol. Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1 Q2 Q3 Q4 T Dallas Legion 2 1 7 7 17 Austin Sol 9 10 6 6 31 Team Stats Dallas Legion Austin Sol Completions 89% (254/285) 93% (224/240) Hucks 50% (11/22) 79% (11/14) Hold % 33% (11/33) 63% (12/19) O-Line Conversion % 30% (11/37) 50% (12/24) Break % 32% (6/19) 58% (19/33) D-Line Conversion % 55% (6/11) 79% (19/24) Red Zone Conversion % 73% (11/15) 90% (19/21) Blocks 8 14 Turnovers 31 16 Austin demolishes Dallas Considering that Dallas used to absolutely own Austin, it was absolutely staggering to see the halftime score of their 26th all-time meeting this past Saturday night. The Sol led the Legion 19-3 through two quarters. That’s no typo. Nineteen to three! “19-3 is quite unusual, indeed,” said Austin’s Kyle Henke. “Most of the opportunities for breaks were handed to us, but I’m super proud of the way our D-lines pushed those in at a high conversion rate.” Dallas looked a whole lot more like an AUDL team in the second half, where they actually outscored Austin 14-12, but the Sol’s 31-17 victory was still its largest ever margin of victory against their long-time Texas rival. “As we went into this game, I personally believe we were both prepared mentally and physically,” said Dallas’ Connor DeLuna. “This preseason has been nothing but consistency, commitment, and hard work from the entire team and something that myself and leadership have been pushing. From that perspective, we were prepared. However, the first half of the game was pretty defeating and not the type of ultimate I have been consistently seeing every week from the team. I would like to blame this first half on first-game jitters because we had about a third of our team making their debut AUDL start.” The Legion will look to bounce back in their first ever meeting against the Houston Havoc this coming weekend.",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match8.html", result=result)

@app.route("/match9")
def match9():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You are a reputable sports reporter for the 2023 season of the AUDL, write a three paragraph article with a title about this matchup between the Colorado Summit and the LA Aviators. Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1 Q2 Q3 Q4 T Colorado Summit 4 7 5 2 18 LA Aviators 4 4 1 6 15 Team Stats Colorado Summit LA Aviators Completions 89% (221/247) 89% (240/269) Hucks 40% (4/10) 40% (8/20) Hold % 53% (9/17) 45% (9/20) O-Line Conversion % 32% (9/28) 33% (9/27) Break % 45% (9/20) 35% (6/17) D-Line Conversion % 53% (9/17) 35% (6/17) Red Zone Conversion % 82% (14/17) 71% (12/17) Blocks 17 7 Turnovers 26 29 The reigning top two in the West certainly looked like the division’s standard bearing duo again this past weekend, as Colorado and Salt Lake both swept through their doubleheader road trips with two wins apiece. The Summit led by as many as seven in both of their SoCal contests, ultimately prevailing by a combined 10 goals—seven and three, respectively—against the San Diego Growlers and Los Angeles Aviators, while the Shred required an epic comeback on Friday against Portland prior to their second shredding of Seattle in as many weeks. “We weren’t prepared for Nitro’s intensity,” said Salt Lake’s Sean Connole, trying to explain the Shred’s slow start that had them down 8-3 after 12 minutes in Portland. “I think many of us were still distracted by Utah Wild’s crushing loss to Oregon in overtime [in the preceding Western Ultimate League game at the same stadium]. We weren’t expecting force middle. We had some chemistry and connection issues. Portland wasn’t phased and was feeding off the energy.” The Nitro still led by four with less than three minutes remaining in the third, but Portland’s offense faltered as the Shred made a critical 7-1 run, transforming an 17-13 deficit into a 20-18 lead with less than four minutes to play. Salt Lake’s O-line did the rest, completing one careful pass after another in the closing moments to seal the deal, never again providing Portland with the shot at an equalizer. “We put the D-line in a position that they hadn’t experienced much last season, and they rose to the challenge to chip away at the lead each quarter,” said Connole. A super satisfying road result for Salt Lake doubled as a demoralizing home defeat for Portland, the Nitro’s 10th consecutive loss since starting last year 2-1. Portland travels to Los Angeles and San Diego this coming weekend, with all three teams desperate for their first wins of the year. Those SoCal teams forced 42 Colorado turnovers across the two games, but had little to show for it as the Summit more often than not avoided breaks when their O-line erred. The Growlers and Aviators combined for 25 break chances against Colorado, but managed just nine breaks. Contrastingly, the Summit orchestrated 20 breaks on 38 opportunities in their two-game sweep, in which Jonathan Nethercutt threw 15 assists and eight different Colorado players created multiple blocks. “We came out with a lot of good energy,” said Summit Co-Head Coach Tim Kefalas. “A lot of our preseason practices and minicamps have been wildly windy or really cold and rainy, so it’s been hard to get a lot of good reps, but despite all that people came out and player super hard.",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match9.html", result=result)

@app.route("/match10")
def match10():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You are a reputable sports reporter for the 2023 season of the AUDL, write a three paragraph article with a title about this matchup between the Philadelphia Phoenix and the DC Breeze. Included below are the box score, some team and individual stats, as well as an article about the current context of all the teams in the league. Make sure to include interesting statistics you find. Box Scores Q1 Q2 Q3 Q4 T Philadelphia Phoenix 3 5 5 6 19 DC Breeze 6 5 3 6 20 Team Stats Philadelphia Phoenix DC Breeze Completions 93% (271/290) 94% (267/285) Hucks 57% (8/14) 36% (4/11) Hold % 41% (9/22) 45% (9/20) O-Line Conversion % 36% (9/25) 38% (9/24) Break % 45% (9/20) 50% (11/22) D-Line Conversion % 69% (9/13) 73% (11/15) Red Zone Conversion % 79% (11/14) 100% (13/13) Blocks 12 12 Turnovers 19 18 Another DC-Philly game down to the wire For their third straight regular season matchup, DC escaped against Philly with a narrow, uncomfortable one goal win. “Another one point loss to DC,” said Phoenix Captain Sean Mott, via the team’s Instagream. “Seems to be a theme.” The Breeze led by five in the first half before their offense experienced uncharacteristic sloppiness. DC finished with a hold rate under 50 percent for just the 11th time in 118 games across the franchise’s history; this was only the second time the Breeze won despite that scale of struggle, joining a 14-13 win over New York from July of 2014. Philadelphia recorded nine breaks, but the Phoenix O-line could not find consistency either, and they were broken 11 times by the Breeze. It was the first time ever that Philly registered more than seven breaks and still lost the game. Greg Martin scored five goals, including a thrilling layout Callahan, to lead the Phoenix, while Moussa Dia and Alexandre Fall each scored four goals from the Breeze’s D-line. Rowan McDonnell fished six assists while playing a team-high 25 points, while Mott played 26 points and totaled 594 yards of offense, though it was all for nought. “I think we’ll have another heated battle against [the Breeze] in Philly,” said Mott.",
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=3,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match10.html", result=result)