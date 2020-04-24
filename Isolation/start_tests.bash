python -c "from AlphaBetaPerformanceTests import *; minmax_vs_semi_radom(50, 3, MeasureOneToTwoFactory, 'MinMax_vs_SemiRandom_50_3_Simple.csv', 'MinMax_vs_SemiRandom_50_3_Simple_GameResult.csv')" > /dev/null &

python -c "from AlphaBetaPerformanceTests import *; minmax_vs_semi_radom(10, 2, MeasureOneStepFurtherFactory, 'MinMax_vs_SemiRandom_10_2_Complex.csv', 'MinMax_vs_SemiRandom_10_2_Complex_GameResult.csv')" > /dev/null &

python -c "from AlphaBetaPerformanceTests import *; minmax_vs_minmax(30, 3, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_White_30_3_Simple.csv', 3, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_Black_30_3_Simple.csv', 'MinMax_vs_MinMax_30_3_Simple_3_Simple_GameResult.csv')" > /dev/null &

python -c "from AlphaBetaPerformanceTests import *; minmax_vs_minmax(20, 3, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_White_20_3_Simple.csv', 4, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_Black_20_4_Simple.csv', 'MinMax_vs_MinMax_20_3_Simple_4_Simple_GameResult.csv')" > /dev/null &

python -c "from AlphaBetaPerformanceTests import *; minmax_vs_minmax(10, 2, MeasureOneStepFurtherFactory, 'MinMax_vs_MinMax_White_10_2_Complex.csv', 2, MeasureOneToTwoFactory, 'MinMax_vs_MinMax_Black_10_2_Simple.csv', 'MinMax_vs_MinMax_10_2_Complex_2_Simple_GameResult.csv')" > /dev/null &



