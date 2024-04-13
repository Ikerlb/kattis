# ls *.txt | cat | python sol.py

nums=$(ls *.ans | wc -l)

for i in $(seq 1 $nums)
do
	cat $i.in | go run sol.go | python evaluate.py
done
