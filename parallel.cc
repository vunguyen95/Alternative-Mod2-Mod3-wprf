#include<random>
#include<algorithm>
#include<cstdlib>
#include<cassert>
#include<set>
#include<thread>
#include<future>
#include<iostream>
using namespace std;
//Key_Gen
vector<int> keyGen(int& length, int& weight){
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distrib(0, length);
    vector<int> key(length);
    for(int j =0; j < length; j++){
        auto temp = distrib(gen);
        if (temp <= weight){
            key[j] = 1;
        }
    }
    return key;
}
//Sample_Gen
vector<int> errorGen(int& length){
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distrib(0,1);
    vector<int> temp(length);
    for(int j = 0; j < length; j++){
        temp[j] = distrib(gen);
    }
    return temp;
}
//XOR
vector<int> add( vector<int> u,  vector<int> v){
	assert(u.size() == v.size());
    vector<int> res(u.size());
	for (int i = 0; i < u.size(); i++){
		res[i] = (u[i] ^ v[i]);
	}
	return res;
}
int weight(vector<int>& u){
    return count(u.begin(),u.end(),1);
}
int weight_short(vector<int>& u){
    return count(u.begin()+1,u.end(),1);
}
//generating x' so that (x,x') = weight that can split into two parts.
vector<int> pairGen(vector<int>& v, int& l){
    vector<int> temp(v.begin(), v.end());
    auto length = v.size()-1;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distrib(0,length);
    vector<int> position_zero;
    vector<int> position_one;
    if(weight(v) < l || (length + 1 - weight(v)) < l){
        cout << "Problem here" << endl;
    }
    while(position_zero.size() < l){
        auto pos = distrib(gen);
        if(v[pos] == 0){
            if(find(position_zero.begin(),position_zero.end(),pos)== position_zero.end()){
                position_zero.emplace_back(pos);
            }
        }
    }
    while(position_one.size() < l){
        auto pos = distrib(gen);
        if(v[pos] == 1){
            if(find(position_one.begin(), position_one.end(), pos)== position_one.end()){
                position_one.emplace_back(pos);
            }
        }
    }
    assert(position_zero.size() == position_one.size());
    /*cout << position_zero.size() << endl;
    cout << position_one.size() << endl;
    cout << position_zero;
    cout << position_one;*/
    for(int j = 0; j < position_zero.size(); j++)
    {
        assert(v[position_zero[j]] == 0);
        temp[position_zero[j]] = 1;
    }
    for(int j = 0; j < position_one.size(); j++)
    {
        assert(v[position_one[j]] == 1);
        temp[position_one[j]] = 0;
    }
    return temp;
}

int sum_mod6(vector<int>& k, vector<int>& sample){
    assert(k.size() == sample.size());
    int sum{0};
    for(int j = 0; j < k.size(); j++){
        sum = (sum + k[j]*sample[j])%6;
    }
    return sum;
}
int prf(vector<int>& k, vector<int>& sample){
    assert(k.size() == sample.size());
    auto temp = sum_mod6(k,sample);
    if(temp == 0 || temp == 1 || temp == 2){
        return 0;
    }
    else{
        return 1;
    }

}// OK
int prf1(vector<int>& k, vector<int>& sample){
    int sum2{0};
    int sum3{0};
    for(int j = 0; j < k.size(); j++){
        sum2 = (sum2 + k[j]*sample[j])% 2;
        sum3 = (sum3 +k[j]*sample[j])% 3;
    }
    return (sum2 + sum3)%2;
}


int main_func(int length, float samples, int l){
    int res{0};
    set<vector<int>> mySet;
    vector<int> key = errorGen(length);
    while(weight(key) < length/2 - 5 || weight(key)> length/2 +5){
            key = errorGen(length);
        }
    while(mySet.size() < samples){
        auto temp = errorGen(length);
        if( prf(key,temp) == 0){
            mySet.insert(temp);
        }
    }
    for( auto it = mySet.begin(); it != mySet.end(); it++ ){
        auto v = *it;
        auto temp = pairGen(v,l);
        auto sum = add(v,temp);
        assert( weight(sum) == 2*l );
        if(prf(key,temp) == 0){
            res++;
        }
    }
    return res;
}

//Multithreading version
int main()
{
    int length = 384;
    float samples = 100000;
    int nthreads = 12;
    vector<int> results(nthreads);
    vector<future<int>> futures(nthreads);
    int w = 310;
    int l = 12;
    std::cout << l << endl;
    std::cout << "Total sample per thread: " << samples << endl;
   

    for(decltype(futures)::size_type i = 0; i< nthreads; i++){
        futures[i] = std::async(main_func, length, samples, l);
    }
    for(decltype(futures)::size_type i = 0; i < nthreads; i++){
        results[i] = futures[i].get();
    }
    float result{0};
    for(auto i = 0; i < nthreads; i++){
        result = result + static_cast<float>(results[i]);
    }

    cout << "End generating" << endl;
    cout << (result/(nthreads*samples) - 0.5)<<endl;
    
}