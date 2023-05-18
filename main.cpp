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

//01000001001000000000100110011000001000100001010111011101100100001001110101110011111011011011100000010001101001000101011011001010
