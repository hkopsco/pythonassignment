#!/usr/bin/env python3

from count_kmers import count_kmers
import pytest

#test that k = 3 is 64
def test_count_kmers(fasta):
    counter = count_kmers(2,fasta,{})
    assert len(counter) == 64

#test that k = 0 is 0
def test_kmers0(fasta):
    counter = count_kmers(0,fasta,{})
    assert len(counter) == 0

#test that k = 1000 is 0
def test_kmers1000(fasta):
    counter = count_kmers(1000,fasta,{})
    assert len(counter) == 0

#test that k = -4 is 0
def test_kmers_neg(fasta):
    counter = count_kmers(-4,fasta,{})
    assert len(counter) == 0

#test k = -2 produces 0
def test_count_kmers_neg(fasta):
    counter = count_kmers(-2,fasta,{})
    assert len(counter) == 0
