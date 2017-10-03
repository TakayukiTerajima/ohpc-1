#!/bin/sh

echo " "
echo " "
echo "-----------------------------------------------------------------"
echo "SCOTCH tests Start"
echo "-----------------------------------------------------------------"

rm -rf res out
touch res
./test_common_random tmp/rand.dat 0 2>&1 >> out
./test_common_random tmp/rand.dat 1 2>&1 >> out
./test_common_thread 2>&1 >> out
./test_strat_seq 2>&1 >> out
./test_scotch_graph_coarsen data/bump_b1.grf 2>&1 >> out
./test_scotch_graph_coarsen_build data/bump.grf 2>&1 >> out
./test_scotch_graph_coarsen_build data/bump_b1.grf 2>&1 >> out
./test_scotch_graph_color data/bump.grf 2>&1 >> out
./test_scotch_graph_map data/m4x4.grf 2>&1 >> out
./test_scotch_graph_map data/m4x4_b1.grf 2>&1 >> out
./test_scotch_graph_map data/m16x16.grf 2>&1 >> out
./test_scotch_graph_map data/m16x16_b1.grf 2>&1 >> out
./test_scotch_graph_map_copy data/bump_b1.grf 2>&1 >> out
./test_scotch_graph_order data/bump.grf 2>&1 >> out
./test_scotch_graph_order data/bump_b1.grf 2>&1 >> out
./test_scotch_graph_part_ovl 4 data/m16x16.grf /dev/null 2>&1 >> out
./test_scotch_graph_part_ovl 4 data/m16x16_b1.grf /dev/null 2>&1 >> outes
gord data/bump.grf /dev/null -vt 2>&1 >> out
gord data/bump_b1.grf /dev/null -vt 2>&1 >> out
gpart 32 data/bump_imbal_32.grf /dev/null -rodata/bump_old.map -vmt 2>&1 >> out

echo " "
grep -e "ERROR" -e "FAILED"  -e "suspicious" -e "illegal" res
if [ $? -ne 1 ]; then
    exit 1
fi
exit 0

