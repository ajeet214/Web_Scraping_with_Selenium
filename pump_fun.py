"""
Author: Ajeet
Created: 1/6/2025
Description:
    This script automates the process of interacting with the 'https://pump.fun' website.
    It performs the following actions:
    1. Bypasses automation detection using custom Chrome options.
    2. Clicks the "I'm ready to pump" button on a pop-up.
    3. Handles the "Reject All" cookies dialog.
    4. Retrieves and processes specific elements matching a CSS selector pattern.
    5. Prints the total count and content of the matching elements.

Project: Automation
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options to bypass automation detection
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Initialize the WebDriver with the specified options
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Navigate to the target URL
driver.get('https://pump.fun')
# Initialize an explicit wait with a timeout of 10 seconds
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Wait for the "I'm ready to pump" button to appear and click it
    ready_button = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#radix-\:r0\: > div.mt-3 > button')
    ))
    ready_button.click()

    # Step 2: Wait for the "Reject All" cookies button to appear and click it
    cookies_button = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#btn-reject-all")
    ))
    cookies_button.click()

    # Step 3: Wait for the visibility of all div elements with IDs ending in "pump" and retrieve them
    div_elements = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, 'div.grid.grid-col-1>div[id$="pump"]')
    ))

    # Print the total count of matching div elements
    print(f"Total result count: {len(div_elements)}")

    # Step 4: Iterate through the retrieved div elements and print their content
    for idx, div in enumerate(div_elements, start=1):
        print(f"------------ {idx} result ------------")
        print(div.text)  # Visible text content of the div

except Exception as e:
    # Handle unexpected errors and print the error message
    print(f"An unexpected error occurred: {e}")

finally:
    # Ensure the driver is closed to release resources
    driver.quit()

"""
output:
Total result count: 46
------------ 1 result ------------
created by
DoSVMa
1h ago
market cap: $18.2K
replies: 40
OFFICIAL TRUMP FAMILY (OTF): OFFICIAL TRUMP FAMILY
------------ 2 result ------------
created by
A4FACP
1d ago
market cap: $13.0K
replies: 20
NexantAI (NEXANT): Nexant – the AI agent with a mission to build the most groundbreaking blockchain ever. Powered by limitless knowledge, cutting-edge innovation, and a sprinkle of chaotic genius, Nexant is here to redefine decentralization. 🌌💡
------------ 3 result ------------
created by
DcpAyb
9h ago
market cap: $67.0K
[
]
replies: 317
Apeshit Alvin (Alvin): doing apeshit things with Alvin.
------------ 4 result ------------
created by
129uzz
5m ago
market cap: $7.0K
replies: 6
Donald Pump (DNLDPMP): Never sell this coin just buy a dollar worth and we will get rich!
------------ 5 result ------------
created by
GwTgqv
3h ago
market cap: $15.2K
replies: 287
Official Melania Fart Coin (OMFC): Melania Trumps Official Fart Coin is here to set the world ablaze. Her looks are breath taking and her farts are astronomical and magical. Come get a wiff of the absolute magnificent smell of the first lady's farts
------------ 6 result ------------
created by
CVvJnD
35m ago
market cap: $7.3K
replies: 11
U Should Do Time (USDT):
------------ 7 result ------------
created by
zJfoJE
18h ago
market cap: $7.3K
replies: 10
Trump and Elon (Trump&Elon): Tump&Elon official
------------ 8 result ------------
created by
Eysnef
6h ago
market cap: $29.2K
[
]
replies: 128
Barron Meme (BARRON): Barron Meme
------------ 9 result ------------
created by
BJN3k9
31m ago
market cap: $9.1K
replies: 23
EarCoin (EarCoin): *** NO UTILITY, JUST FOR THOSE WHICH LOVE TRUMP
------------ 10 result ------------
created by
FbXpLa
32m ago
market cap: $4.8K
[
]
replies: 20
Official X Rat Wif Hat (RATWIFHAT):
------------ 11 result ------------
created by
Fg7fFK
38m ago
market cap: $7.2K
replies: 38
DONA TRUMPINA (FIRSTLADY): DONA TRUMPINA
------------ 12 result ------------
created by
5BCkFt
41m ago
market cap: $6.8K
replies: 19
Official Vise President (JD Vance):
------------ 13 result ------------
created by
GtdNeB
5h ago
market cap: $321.5K
[
]
replies: 199
Be Best (BB):
------------ 14 result ------------
created by
9W1L5Y
13d ago
market cap: $7.5K
replies: 30
TRUMP BUTTHOLE FART NUTS (TBHFN): 🇺🇲
------------ 15 result ------------
created by
7AkdDR
17m ago
market cap: $7.3K
replies: 15
I HAVE A COIN (IHAVEACOIN):
------------ 16 result ------------
created by
Fq1R9G
56m ago
market cap: $7.5K
replies: 17
Captain America Melania (CAM): Captain America Melania
------------ 17 result ------------
created by
DsXDQs
38m ago
market cap: $7.5K
replies: 8
Javier Milei Official (Milei): The Official Milei Argentina is live!
------------ 18 result ------------
created by
5h7Ymr
6h ago
market cap: $15.4K
replies: 52
Ivanka (IVANKA):
------------ 19 result ------------
created by
8bTDDQ
27m ago
market cap: $7.3K
replies: 7
LeBarron James (LEBARRON):
------------ 20 result ------------
created by
7bueRj
9h ago
market cap: $31.0K
replies: 53
Weber AI (WEBAI): Launch your memecoin website instantly. An AI powered tool leveraging prompt-to-CSS technology and fine-tuned for memecoin themes.
------------ 21 result ------------
created by
4Gbd3n
10m ago
market cap: $7.0K
replies: 16
This is the sky (Tits):
------------ 22 result ------------
created by
4FxSjy
1h ago
market cap: $8.0K
replies: 11
$TTDS Defends Freedom of Speech (TTDS ): Trump Saves TikTok. Defends Freedom of Speech MEME $TTDS President Trump turned the tide, saved TikTok, and defended the American people's freedom of speech!
------------ 23 result ------------
created by
4QW2bE
17m ago
market cap: $7.3K
replies: 10
GOD Sent Us Trump (GSUT): GOD sent us trump to fill our bags. In a world where memes drive the culture, God Sent Us Trump is here to make its mark! This token celebrates the spirit
 of unshakable leadership, bold visions, and the meme-worthy moments that brought us together. Whether you see Trump as a divine blessing, a larger-than-life icon, or the ultimate meme muse, this token captures it all in a fun, lighthearted way!
------------ 24 result ------------
created by
8bVKXK
3h ago
market cap: $7.4K
replies: 13
OFFICIAL CREED (CREED): The official Creed Coin! Can take me higher!
------------ 25 result ------------
created by
972BGm
2h ago
market cap: $17.2K
[
]
replies: 51
Donald Trump Family 6900 (DTF6900): An index tracking the performance of the Trump family memes.
------------ 26 result ------------
Video
created by
7rmUwY
4h ago
market cap: $7.0K
replies: 12
Bank of Ai Agents (BankofAi): Welcome to Bank of Ai, where we revolutionize the way token holders receive their funds globally. Our cutting-edge technology enables seamless transfe
rs to token holders around the world, ensuring speed and security. Bank of Ai agents are designed to automate the execution of agreements without the need for intermediaries or tim
e delays. Ai Bank agents nodes execute the contract. Your personal Ai Bank agents pay out in USDC around the clock. Each token is one Ai Bank agent. 100 tokens minimum hold for ai 
agent pay. Bank of a i agents are designed to automate the execution of agreements without the need for intermediaries or time delays. Ai Bank agents nodes execute the contract. Yo
ur personal A i Bank agents pay out in USDC around the clock. Each token is one Ai Bank agent. 100 tokens minimum hold for ai agent pay. Be sure to check out our YouTube channel Bank of Ai and Join us! Regards, Agent Ai
------------ 27 result ------------
created by
5zA23t
1h ago
market cap: $8.4K
replies: 127
Elon Trenches Fighter (ETF): AFTER DONALD ELON WILL RULE THE TRENCHES
------------ 28 result ------------
created by
EKRVV5
5m ago
market cap: $7.0K
replies: 4
U Should Dump Crypto (USDC):
------------ 29 result ------------
created by
Bc7azw
37m ago
market cap: $7.2K
replies: 10
Inauguration of (IOS): It’s not only Trumps inauguration. It’s also solana’s.
------------ 30 result ------------
created by
HXfnVz
14m ago
market cap: $18.5K
replies: 31
Tied Up & Tickled Til 50 Mil (Tickled): I haven't found a job yet so I'm doing weird kink shit for money. Tied Up & Tickled until $5 million $500,000 - wedgies $1 million - Visqueen / Slime $3 million marketcap - Pie $4 million - Antiqued $5 million marketcap - Head Shaving, burn dev wallet
------------ 31 result ------------
created by
57Kn8x
9m ago
market cap: $6.8K
replies: 10
AmericaFirst.Fun (FIRST): AmericaFirst.Fun
------------ 32 result ------------
created by
82tLwz
45m ago
market cap: $11.4K
replies: 59
TRUMPIUS MAX (TRUМРIUS): Make Pump Great Again
------------ 33 result ------------
created by
EX8PZk
32m ago
market cap: $6.8K
replies: 9
Rare White Bamby (BAMBY): Rare White Bamby
------------ 34 result ------------
Video
created by
DrGA8L
2 months ago
market cap: $6.9K
replies: 9
Purgatory ($INNER): From dust, we are created, and dust we will return. We are the disobedient.
------------ 35 result ------------
created by
7BgTDJ
3h ago
market cap: $104.8K
[
]
replies: 74
Trump Family Index (TFI500): Trump Family Index
------------ 36 result ------------
created by
8pijxj
6h ago
market cap: $12.6K
[
]
replies: 74
Ninicoin (Nini): Tao Lin cure my poverty
------------ 37 result ------------
created by
J1AoDU
9h ago
market cap: $29.1K
[
]
replies: 304
President Troog (Troog): It’s huge, folks. President Troog learns it’s connected to the stars—big cosmic secrets, the best secrets. Look for artifacts. Trust me, it’s going to be tremendous!
------------ 38 result ------------
created by
4dMoLv
3h ago
market cap: $7.7K
replies: 22
Baby Elon Musk (BabyElon): We’re going to win so much. You’re going to get tired of winning. You’re going to say, ‘Please, Mr. Baby Elon, I have a headache. Please, I don’t want to win so much. This is getting terrible.’ And I’m going to say. "We’re going to keep winning, winning, winning!"
------------ 39 result ------------
created by
FweAHC
5d ago
market cap: $8.3K
replies: 82
SLIPPAGE (SLIPPAGE):
------------ 40 result ------------
created by
6KeWLf
14m ago
market cap: $13.5K
replies: 11
FredTrump (Fredytrump): The strength of a nation lies in its unity, and its foundation is laid by the wisdom and sacrifices of its fathers.
------------ 41 result ------------
created by
9KCsAb
1h ago
market cap: $17.1K
[
]
replies: 261
First Lady I'd Like to Fuck (FLILF):
------------ 42 result ------------
created by
ApJZ7m
22h ago
market cap: $31.9K
replies: 56
OFFICIAL BARRON (BARRON): Join the Barron Community. This is History in the Making!
------------ 43 result ------------
created by
GPxr6P
44m ago
market cap: $6.7K
[
]
replies: 45
#RapeMarkAndrews (RAPE): #RapeMarkAndrews
------------ 44 result ------------
created by
5GJKpf
5h ago
market cap: $10.7K
replies: 103
Make it all back 100x coin (100x): Make it all back 100x with this coin
------------ 45 result ------------
created by
6xsqu6
4h ago
market cap: $162.7K
[
]
replies: 87
First Nude Lady (Milfania): Official First Nude Lady Milfania meme.
------------ 46 result ------------
created by
6ZFxci
6m ago
market cap: $24.4K
replies: 15
OFFICIAL TEANNA (TEANNA):
"""
# stackoverflow link: https://stackoverflow.com/a/79331894/11179336