# Creating Random data for synthetic data set

The scrip provided here create random data for a synthetic data set.

The script *create_random_objects.sh* shall be executed with the following arguments:

```shell
sh create_random_objects.sh list.txt num_copies

echo "Running this script requires two arguments:"
echo "   1. File path of object sizes information (list.txt)"
echo "   2. Number of objects created for each item in the list of objects given as argument (num_copies)"	
```

This *create_random_objects.sh* script will read *list.txt* file and for each pair (*OBJ*|*SIZE*) found, it will create a random object named *OBJ* with *SIZE* bytes using the */dev/urandom* library of Linux operating system.

Besides, the script will also create *num_copies* duplicates of each object found in the *list.txt* file and call an auxiliary python script (*random_noise_alg.py*) to perform several changes on each copy. The percentage of bytes changes is defined hard-coded.

The purpose of this script is to create a synthetic data set for evaluating the *Approximate Matching* functions, by creating objects with known groundtruth so similarity can be properly measured by these functions.