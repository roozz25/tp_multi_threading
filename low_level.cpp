#include <cpr/cpr.h>
#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <string>
#include <Eigen/Dense>
#include <chrono>

using json = nlohmann::json;
using namespace std;
using namespace std::chrono; 
class Task{
    public:
    Eigen::MatrixXf a;
    Eigen::VectorXf b;
    Eigen::VectorXf x; 
    int size;
    int identifier;
    float time;


    Task()
    {
        cpr::Response r = cpr::Get(cpr::Url{"http://127.0.0.1:8000"},
        cpr::Bearer{"Maxoff"});
        //std::cout << "Response JSON: " << r.text << std::endl;
        json taskj = json::parse(r.text); 
        auto a_mat = taskj["a"];
        auto b_vec = taskj["b"];
        auto x_vec = taskj["x"];
        size = taskj["size"];
        identifier = taskj["identifier"]; 
        int a_lig = a_mat.size();
        int a_col = a_mat[0].size();


        a.resize(a_lig,a_col);

        for(int i = 0; i < a_lig; i++){
            for(int j = 0; j  < a_col; j++){
                a(i,j) = a_mat[i][j];
            }
        }

        int  b_lig = b_vec.size();
        b.resize(b_lig);
        for(int i = 0; i < b_lig ; i++){
            b(i) = b_vec[i];
        }

        x.resize(b_lig);
        


        
    }

    void work(){
       auto start = high_resolution_clock::now();
        
        x = a.colPivHouseholderQr().solve(b);
        //nnnnnnnn
        auto end = high_resolution_clock::now();

        time = duration<float>(end - start).count();
    }

    json to_json() {

    json j;
    j["identifier"] = identifier;

    j["a"] = json::array();
    for (int i = 0; i < a.rows(); ++i) {
      json row = json::array();
      for (int j = 0; j < a.cols(); ++j) {
        row.push_back(a(i, j));
      }
      j["a"].push_back(row);
    }

    j["b"] = json::array();
    for (int i = 0; i < b.size(); ++i) {
      j["b"].push_back(b(i));
    }

    j["x"] = json::array();
    for (int i = 0; i < x.size(); ++i) {
      j["x"].push_back(x(i));
    }

    j["time"] = time;
    j["size"] = size;
    return j;

    }

    void post_result(Task task) {
        json post_data = task.to_json();

        cpr::Response r = cpr::Post(cpr::Url{"http://127.0.0.1:8000"}, cpr::Body{post_data.dump()},
                cpr::Header{{"Content-Type", "application/json"}});
        if (r.status_code != 200) {
            cerr << "HTTP POST failed with status: " << r.status_code << endl;
        } else {
            cout << "Task results (" << task.identifier;
            cout << ") successfully posted!" << endl;
            cout << "Task duration: " << task.time << " seconds" << endl;
            cout << "Task X: " << task.x << endl;
        }
    }
    

    
};

int main(int argc, char** argv) {
    while (true) {
        try {
            Task task = Task();
            task.work();
            task.post_result(task);
        } catch (const std::exception &e) {
            cerr << "An error occurred: " << e.what() << endl;
            return EXIT_FAILURE;
        }
  }
    


    
    return 0;
}