#include <iostream>
#include <vector>
using namespace std;

class node {
	public:
	int data;
	node* child1, *child2, *child3;
	node(int data) {
		this->data = data;
		child1 = NULL;
		child2 = NULL;
		child3 = NULL;
	}
};

pair<int, int> countEvenHelper(node* root) {
	if(root==NULL) return make_pair(0,0);
	if(root->child1==NULL && root->child2==NULL && root->child3==NULL) {
		if(root->data==0) return make_pair(0,0);
		return make_pair(1,0);
	}
	
	vector<pair<int, int> > arr(3);
	arr[0] = countEvenHelper(root->child1);
	arr[1] = countEvenHelper(root->child2);
	arr[2] = countEvenHelper(root->child3);
	
	int evenCount=0, nodeCount=1;
	if(root->data==0) nodeCount = 0;
	
	for(int i=0;i<3;i++) {
		evenCount+= arr[i].second;
		if(arr[i].first >0 && arr[i].first %2==0) evenCount++;
		nodeCount+= arr[i].first;
	}
	return make_pair(nodeCount, evenCount);
}

int countEven(node* root) {
	pair<int, int> totalCntEvenCntPair = countEvenHelper(root);
	return totalCntEvenCntPair.second;
}

int main() {
	// your code goes here
	node* root = new node(1);
	root->child1 = new node(3);
	root->child2 = new node(0);
	root->child3 = new node(2);
	root->child1->child1 = new node(4);
	root->child2->child1 = new node(8);
	root->child3->child1 = new node(7);
	root->child3->child2 = new node(5);
	root->child2->child1->child1 = new node(9);
	//root->child2->child1->child2 = new node(10);
	cout<<countEven(root);
	return 0;
}
