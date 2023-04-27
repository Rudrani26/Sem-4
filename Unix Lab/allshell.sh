#count number of lines words & characters

file="check.txt"

nol=`wc -l < $file`
now=`wc -w < $file`
noc=`wc -c < $file`

echo "Number of lines : $nol"
echo "Number of words : $now"
echo "Number of characters : $noc"

#Command line Input Area and Perimeter

echo "Length : $1"
echo "Breadth : $2"

peri=$((2*($1+$2)))
area=$(($1*$2))

echo "Perimeter : $peri"
echo "Area : $area"

#User input Area and Perimeter

echo "Enter length: "
read l
echo "Enter breadth: "
read b

peri=$((2*($l+$b)))
area=$(($l*$b))

echo "Area is $area"
echo "Perimeter is $peri"

#Simple Interest

echo "Enter P: "
read p
echo "Enter R: "
read r
echo "Enter T: "
read t

si=$((($p*$r*$t)/100))

echo "Simple Interest is $si"

#for command line input 

si=$((($1*$2*$3)/100))

echo "Simple Interest is $si"

#Largest number 

echo "Num 1 :"
read num1
echo "Num 2 :"
read num2
echo "Num 3 :"
read num3

if [ $num1 -gt $num2 ] && [ $num1 -gt $num2 ]
then
	echo "Largest is $num1"
elif [ $num2 -gt $num1 ] && [ $num2 -gt $num3 ]
then
	echo "Largest is $num2"
else 
	echo "Largest is $num3"
fi

#Leap Year

echo "Enter a year: "
read year

if [ `expr $year % 4` -eq 0 ] || [ `expr $year % 400` -eq 0 ]
then 
	echo "It is a leap year" 
else 
	echo "It is not a leap year"
fi

#Multiplication Table

echo "Enter a number: "
read n

i=1

while [ $i -le 10 ]
do
	echo "$n x $i = $((n * i))"
	i=$((i + 1))
done

#Check if element is present in list

echo "Enter elements in an array"
read -a array

echo "Enter element to be searched"
read num

for val in "${array[@]}"
do
	if [ $num -eq $val ]
	then 
		echo "element found"
		exit
	else
		continue
		echo "element not found"
	fi
done

#Compare two strings

echo "Enter first string: "
read str1

echo "Enter second string: "
read str2

if [ $str1 == $str2 ]
then 
	echo "Strings are equal"
else
	echo "Strings are not equal"
fi

#Checking if a file exists if not creating it

echo "enter file name: "
read file 

if [ -f $file ]
then
	echo "File exists"
else
	echo "File doesnt exist"
	echo "Creating the file"
	touch $file
fi

#menu driven calculator

sum=0
i="y"

echo "Num1 : "
read num1
echo "Num2 : "
read num2

while [ $i="y" ]
do
	echo "1.Add"
	echo "2.Sub"
	echo "3.Mult"
	echo "4.Div"
	echo "Enter your choice: "
	read ch
	
	case $ch in
		1) sum=`expr $num1 + $num2`
		echo "$sum";;
		2) sub=`expr $num1 - $num2`
		echo "$sub";;
		3) multi=`expr $num1 \* $num2`
		echo "$multi";;
		4) div=`expr $num1 / $num2`
		echo "$div";;
		*)echo "Invalid choice";;
	esac
	
	echo "Continue? [y/n]"
	read i
	if [ $i != "y" ]
	then
		exit
	fi
done 

#pattern

echo "rows: "
read rows

for ((i=1; i<=$rows; i++))
do
	for ((j=1; j<=i; j++))
	do
		echo -n "* "
	done
	echo
done





