from isla.parser import EarleyParser
from evogfuzz.probabilistic_fuzzer import ProbabilisticGrammarMinerExtended

def get_final_grammar(grammar, test_inputs):
    probabilistic_grammar_miner = ProbabilisticGrammarMinerExtended(EarleyParser(grammar))

    probabilistic_grammar = (
        probabilistic_grammar_miner.mine_probabilistic_grammar(test_inputs)
    )
    return probabilistic_grammar
