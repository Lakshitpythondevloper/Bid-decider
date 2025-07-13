# 🏆 Bid-decider

A Python project to help you make smarter, data-driven decisions for bids, auctions, or competitive offers.  
**Bid-decider** aims to bring intelligence, fairness, and automation to your bidding process.

---

## 🚀 Features

- **Automated Decision-Making**: Streamline and automate bid selections using Python logic.
- **Customizable Logic**: Adaptable for different bidding scenarios—auctions, tenders, competitions, and more.
- **Open Source**: Licensed under the MIT License for maximum flexibility.
- **Easy to Extend**: Simple architecture to add your own rules or analytics.

---

## 📦 Installation

```bash
git clone https://github.com/Lakshitpythondevloper/Bid-decider.git
cd Bid-decider
# (Optional) Create a virtual environment:
# python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

---

## ⚙️ Usage

1. **Configure your bid data or logic** in the main Python script.
2. **Run the application**:
   ```bash
   python main.py
   ```
3. **View results**: The program will output the recommended bid decision based on your logic.

---

# Auction Bidding Program

A simple console-based auction bidding program written in Python that allows multiple users to place bids and determines the winner with the highest bid.

## Code Overview

```python
import logo

print(logo)
def highest_number(biddest_number):
    score = 0
    winner = ""

    for high in biddest_number:
        number = biddest_number[high]

        if number > score:
            score = number
            winner = high
    print(f"Okay! The winner is {winner} and the bid is {score} $ 😀")

bid = {}
Programme_end = True

while Programme_end:

    user_name = input("What is your name: ").title()
    user_bide = int(input("What is your bid $: "))
    bid[user_name] = user_bide
    any_biders = input("If there is any biders type 'yes' or 'no': ").capitalize()

    if any_biders == 'Yes':
        print("\n"*100)
    if any_biders == 'No':
        Programme_end = False
        highest_number(biddest_number = bid)
```

## Detailed Code Explanation

### Imports and Initial Setup
```python
import logo
print(logo)
```
- The program imports a custom `logo` module (not shown in the code)
- Displays the logo at the start of the program

### Highest Bid Function
```python
def highest_number(biddest_number):
    score = 0
    winner = ""

    for high in biddest_number:
        number = biddest_number[high]

        if number > score:
            score = number
            winner = high
    print(f"Okay! The winner is {winner} and the bid is {score} $ 😀")
```
- Function `highest_number` takes a dictionary of bidders and their bids as input
- Initializes variables `score` (to track highest bid) and `winner` (to store winner's name)
- Iterates through the dictionary to find the highest bid
- Updates `score` and `winner` when a higher bid is found
- Prints the winner and their winning bid amount

### Main Program Logic
```python
bid = {}
Programme_end = True
```
- Creates an empty dictionary `bid` to store bidder names and their bids
- `Programme_end` controls the main program loop

### Bidding Loop
```python
while Programme_end:
    user_name = input("What is your name: ").title()
    user_bide = int(input("What is your bid $: "))
    bid[user_name] = user_bide
    any_biders = input("If there is any biders type 'yes' or 'no': ").capitalize()
```
- Continuously asks for bids until stopped
- Gets bidder's name and converts it to title case
- Gets bid amount and converts it to integer
- Stores the bid in the dictionary with name as key and bid as value
- Asks if there are more bidders

### Program Flow Control
```python
    if any_biders == 'Yes':
        print("\n"*100)
    if any_biders == 'No':
        Programme_end = False
        highest_number(biddest_number = bid)
```
- If there are more bidders (`'Yes'`), clears the screen by printing 100 newlines
- If no more bidders (`'No'`), ends the program and determines the winner

## How to Use

1. Run the program
2. Enter your name when prompted
3. Enter your bid amount
4. Indicate if there are more bidders:
   - Type 'yes' to continue accepting bids
   - Type 'no' to end bidding and determine the winner
5. The program will display the winner and their bid amount

## Features

- Accepts multiple bids from different users
- Clears screen between bids for privacy
- Automatically determines highest bidder
- User-friendly interface with emoji output
- Case-insensitive input handling

## Note

The program requires a separate `logo` module which should be in the same directory. Make sure to have this file available before running the program.

## ASCII art in logo.py

```python
                                                                      
                                                                                                    
                                           ██████████                                               
                                         █████████████                                              
                                        ███████████████                                             
                                      ███████     █████                                             
                                   ████████      ██████                                             
                                  ███████      ████████                                             
                                ████████     ████████████                                           
                              ████████      ███████████████                                         
                             ███████      ████████  ████████                                        
                          ████████      ███████        ████████                                     
                         ███████      ███████           █████████                                   
                         █████      ████████              ████████                                  
                         ██████    ███████                  ████████                                
                         ███████████████                     █████████                              
                           ██████████████                       ██████████████                      
                              ██████████████                     ███████████████                    
                                   ██████████                   ███████   ██████                    
                                 ██████████████               ████████     █████                    
                                █████████████████           ████████      ██████                    
                                ███████   ████████         ███████      ████████                    
                              ███████████    ████████   ████████      ███████                       
                             ██████████████   ████████████████      ███████                         
                           ████████ ████████████████████████      ████████                          
                         ████████     █████████████████████      ███████                            
                        ███████        ██████████████████      ███████                              
                      ███████        ██████████   █████      ███████                                
                    ███████        ███████        ███████  ███████                                  
                  ███████        ███████           ██████████████                                   
                ████████       ████████             ███████████                                     
               ███████        ███████                  █████                                        
             ███████        ███████                                                                 
          ████████       ████████                                                                   
         ███████        ███████                                                                     
        ███████       ████████                        ███████████████████████████████               
        █████       ████████                        ███████████████████████████████████             
        █████      ███████                         █████████████████████████████████████            
        ███████  ███████                           █████                            █████           
          ████████████                             ██████                          ██████           
           █████████                              ████████████████████████████████████████          
              ███                               ████████████████████████████████████████████        
                                               █████████████████████████████████████████████        
                                               █████                                   █████        
                                               █████████████████████████████████████████████        
                                                ████████████████████████████████████████████        
                                                 █████████████████████████████████████████    
```

## 🛠️ Customization

- Edit the Python files to add or change how decisions are made.
- Integrate with your own data sources or user interfaces as needed.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

- [Lakshitpythondevloper](https://github.com/Lakshitpythondevloper)

---

## 🌟 Contributing

Pull requests and suggestions are welcome!  
Open an issue to discuss improvements or report bugs.

---

## 📚 Resources

- [Project Repository](https://github.com/Lakshitpythondevloper/Bid-decider)

---

> Make your next bid the smartest one yet! 🚀
