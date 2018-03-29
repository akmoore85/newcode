from flask import Flask
from flask import request
node = Flask(__name__)


#Store the transactions that this node has in a list
this_nodes_transactions = []


@node.route('/txion' methods=['POST'])
def transaction():
    if request.method == 'POST':
        #on each new POST request we extract the transaction data
        new_txion = request.get_json()
        #then we add the transaction to our list
        this_nodes_transactions.append(new_txion)
        #Because the transaction was successfully submitted, we log it to our console
        print "New Transaction"
        print "From: {}".format(new_txion['from'])
        print "To: {}".format(new_txion['to'])
        print "Amount: {}\n".format(new_txion['amount'])
        #Then we let the client know it worked out
        return "Transaction submission successful\n"
    node.run()

#blockchain
#Block class definition


def proof_of_work(last_proof):
    #Create a variable that we will use to find our next proof of work
    incrementor = last_proof + 1
    #Keep incrementing the incrementor until it's equal to a number divisible by 9
    #and the proof of work of the previous block in the blockchain
    while not  (incrementor % 9 == 0 and incrementor % last_proof == 0 ):
        incrementor += 1
    #Once that number is found we can return it as a proof of our work
    return incrementor

@node.route('/mine', methods = ['GET'])
def mine():
    last_block = blockchain[len(blockchain) - 1]
