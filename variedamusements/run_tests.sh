# ls *.txt | cat | python sol.py

nums=$(ls *.in | wc -l)

for i in $(seq 1 $nums)
do
	cat $i.in | python sol.py | diff $i.ans -
done
