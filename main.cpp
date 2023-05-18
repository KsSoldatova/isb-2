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