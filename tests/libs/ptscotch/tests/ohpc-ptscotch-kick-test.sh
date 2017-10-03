#!/bin/sh

echo " "
echo " "
echo "-----------------------------------------------------------------"
echo "PTSCOTCH tests Start"
echo "-----------------------------------------------------------------"

rm -rf res out
touch res
./test_strat_par 2>&1 >> out
./test_scotch_dgraph_check data/bump.grf 2>&1 >> out
./test_scotch_dgraph_check data/bump_b1.grf 2>&1 >> out
./test_scotch_dgraph_band data/bump_b1.grf 2>&1 >> out
./test_scotch_dgraph_coarsen data/bump.grf 2>&1 >> out
./test_scotch_dgraph_coarsen data/bump_b1.grf 2>&1 >> out
./test_scotch_dgraph_grow data/bump.grf 2>&1 >> out
./test_scotch_dgraph_redist data/bump.grf 2>&1 >> out
echo " "
grep -e "ERROR" -e "FAILED"  -e "suspicious" -e "illegal" res
if [ $? -ne 1 ]; then
    exit 1
fi
exit 0

