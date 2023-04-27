#check if prime 

print "Enter the number: ";
$num=<>;
chop($num);

$flag=0;

for($i=2;$i<$num;$i++)
{
	if($num % $i==0)
	{
		$flag=1;
		break;
	}
}

if($flag==1)
{
	print "It is not a prime\n";
}
else
{
	print "It is prime\n";
}

#check if leap year

print "Enter the year: ";
$num=<>;

if($num % 4 == 0)
{
	print "It is a leap year\n";
}
else
{
	print "It is not a leap year\n";
}

#sort elements

@numbers=(23,96,57,83,17);
print "Unsorted @numbers\n";
@sorted = sort @numbers;
print "Sorted @sorted\n";





