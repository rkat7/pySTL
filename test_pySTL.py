from pySTLtools import primes_till_, count_set_bits, is_bit_set

def test_primes_till_with_params():
	assert primes_till_(20)==[2,3,5,7,11,13,17,19]

def test_count_set_bits_with_param():
	assert count_set_bits(10)==2

def test_is_bit_set_with_params():
	assert is_bit_set(7,0)==True