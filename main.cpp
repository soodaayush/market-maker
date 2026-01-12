// Planning

// Market - the environment of the program
    // Prices change in both positive and negative direction
    // This simulates real market movement
// Traders - bots
    // Someone wanting to buy and sell stock
    // Amounts are random
// Market Maker (this program)
    // Contains money, shares, spread
    // Consults order book to check buy and sell prices to post them
    // Attempts to make profit through spread
// Trade Engine
    // If trader wants to buy -> engine sells
    // If trader want to sell -> engine buys
// Dashboard
    // What the user sees
    // Shows market price, bid and ask, your inventory, cash, profit,a nd trade history

#include <iostream>
#include <random>

using namespace std;

int main() {
    int time = 1;
    double price = 100;

    random_device rd;

    mt19937 gen(rd());

    uniform_real_distribution<double> dis(-1, 1);

    for (int i = time; i <= 10; i++) {
        double randomPrice = dis(gen);
        price = price + randomPrice;
        cout << "Time: " << i << "  Price: " << price << endl;
    }
}