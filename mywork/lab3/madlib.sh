#!/bin/bash


clear
echo "Let's build a mad-lib!"


read -p "1. Please give me an adjective: " ADJ1
read -p "2. Please give me another adective: " ADJ2
read -p "3. Please give me a noun: " N1
read -p "4. Please give me another noun: " N2
read -p "5. Please give me another noun: " N3
read -p "6. Please give me a verb: " V1
read -p "7. Please give me another verb: " V2
read -p "8. Please give me an adverb: " ADV

echo "Once upon a time, there was a $ADJ1 $N1 that hated going to school."
echo "One day, the $N1 met a new student, who was a $ADJ2 $N2."
echo "The teacher asked $N2 to sit with $N3 and $V1 $ADV the class with $N1."
echo "From then on, they all became best friends and would $V2 together every day."
echo "The end."
