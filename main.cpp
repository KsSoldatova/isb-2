#include <iostream>
#include <random>
#include <ctime>

int main()
{
	std::mt19937 mersenne{ static_cast<std::mt19937::result_type>(std::time(nullptr)) };
	std::uniform_int_distribution<> die{ 0, 1 };
	for (int count{ 1 }; count <= 128; ++count) std::cout << die(mersenne);
	return 0;
}

//00011111010110101001011101010011010101100110000111111110110010010001001001000011001111101011000000100001110011011110010011100101
