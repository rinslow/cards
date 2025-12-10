#!/usr/bin/env python
"""
Simple CLI Game Template
A minimalistic template for building command-line games in Python.
"""
from game import Deck

import sys


class Game:
    """Base game class with core game loop functionality."""
    
    def __init__(self):
        self.running = True
        self.score = 0
        
    def display_welcome(self):
        """Display welcome message."""
        print("=" * 40)
        print("Welcome to the Game!")
        print("=" * 40)
        print()
        
    def display_menu(self):
        """Display game menu."""
        print("\n--- Menu ---")
        print("1. Play")
        print("2. Instructions")
        print("3. Quit")
        print()
        
    def get_user_input(self, prompt: str) -> str:
        """Get input from user with error handling."""
        try:
            return input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGame interrupted. Goodbye!")
            sys.exit(0)
            
    def handle_menu_choice(self, choice: str):
        """Handle menu selection."""
        if choice == "1":
            self.play()
        elif choice == "2":
            self.show_instructions()
        elif choice == "3":
            self.quit()
        else:
            print("Invalid choice. Please try again.")
            
    def play(self):
        """Main game logic - override in subclasses."""
        print("\nGame started!")
        print("This is a template - implement your game logic here.")
        print("Game ended. Score: 0")
        
    def show_instructions(self):
        """Display game instructions."""
        print("\n--- Instructions ---")
        print("This is a template game.")
        print("Implement your game rules here.")
        print()
        
    def quit(self):
        """Exit the game."""
        print("\nThanks for playing! Goodbye!")
        self.running = False
        
    def run(self):
        """Main game loop."""
        self.display_welcome()
        
        while self.running:
            self.display_menu()
            choice = self.get_user_input("Enter your choice: ")
            self.handle_menu_choice(choice)


def main():
    """Entry point for the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    deck = Deck()
    print(deck)
