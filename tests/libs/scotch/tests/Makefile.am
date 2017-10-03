TESTS_ENVIRONMENT = BATS_NO_SUMMARY=1
CLEANFILES        = res out
TESTS             = ohpc-scotch-kick-test.sh
check_PROGRAMS    = test_common_random	\
	             test_common_thread	\
	             test_strat_seq	\
	             test_scotch_graph_coarsen	\
	             test_scotch_graph_coarsen_build	\
	             test_scotch_graph_part_ovl	\
	             test_scotch_graph_color	\
	             test_scotch_graph_map	\
		      test_scotch_graph_order 

dist_noinst_DATA  = $(TESTS)

test_common_random_SOURCES              = test_common_random.c
test_common_thread_SOURCES              = test_common_thread.c
test_strat_seq_SOURCES                  = test_strat_seq.c
test_scotch_graph_coarsen_SOURCES       = test_scotch_graph_coarsen.c
test_scotch_graph_coarsen_build_SOURCES = test_scotch_graph_coarsen_build.c
test_scotch_graph_part_ovl_SOURCES      = test_scotch_graph_part_ovl.c
test_scotch_graph_color_SOURCES         = test_scotch_graph_color.c
test_scotch_graph_map_SOURCES           = test_scotch_graph_map.c
test_scotch_graph_order_SOURCES         = test_scotch_graph_order.c

