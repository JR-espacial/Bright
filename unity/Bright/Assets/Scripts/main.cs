using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Net;
using System.IO;

public class main : MonoBehaviour
{
    public GameObject myPrefab;
    Vector3[] carPositions = {new Vector3(30, 2.5f, 2), new Vector3(-30, 2.5f, -2), new Vector3(-2, 2.5f, 28), new Vector3(2, 2.5f, -28)};
    Vector3[] carRotation = {new Vector3(0, 180, 0), new Vector3(0, 0, 0), new Vector3(0, 90, 0), new Vector3(0, -90, 0)};
    List<List<GameObject>> cars = new List<List<GameObject>>();
    public TrafficLight[] trafficLights = new TrafficLight[4];

    [System.Serializable]
    public class TrafficLightJSON{
        public int id;
        public bool green;
        public TrafficLightJSON(int id_,bool green_){
            id = id_;
            green = green_;
        }
    }
    [System.Serializable]
    public class CarJSON{
        public int id;
        public int destiny;
        public int lane;
        public bool isMoving;
        public CarJSON(int id_,int destiny_, int lane_,bool isMoving_){
            id = id_;
            destiny = destiny_;
            lane = lane_;
            isMoving = isMoving_;
        }
    }

    [System.Serializable]
    public class Cars
    {
        public List<CarJSON> cars;
    }



    private void Start() {
        for (int i = 0; i < carPositions.Length; i++)
        {
            List<GameObject> temp = new List<GameObject>();
            cars.Add(temp);
        }

        newCar(0, 0);
        newCar(1, 2);
        newCar(2, 1);
        newCar(3, 0);

        string jsonString = File.ReadAllText("./test.json");

        // using (WebClient wc = new WebClient()){
        //     var json = wc.DownloadString("https://bright-agentes.us-south.cf.appdomain.cloud/");
        //     string subJson = json.Substring(1, json.Length-3);
        //     TrafficLightJSON data = JsonUtility.FromJson<TrafficLightJSON>(subJson);
        //     print(data.green);  
        // }

        Cars test2 = JsonUtility.FromJson<Cars>(jsonString);
        print(test2.cars[0].lane);

        
        
    }
    
    void Update()
    {   
        //to stop car movement
        //cars[0][0].GetComponent<Car>().setIsMoving(false);
        trafficLights[0].turnYellowOn();
        trafficLights[0].turnRedOn(); 
    }

    void newCar(int lane, int destination){
        Vector3 v = carRotation[lane];
        GameObject car = Instantiate(myPrefab, carPositions[lane], Quaternion.Euler(v.x, v.y, v.z));
        car.AddComponent<Car>();
        car.GetComponent<Car>().setDestination(destination);
        cars[lane].Add(car);
    }

}