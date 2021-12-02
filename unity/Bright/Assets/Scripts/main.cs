using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Net;
using System.IO;

public class main : MonoBehaviour
{
    public GameObject myPrefab;
    Vector3[] carPositions = {new Vector3(30, 0.82f, 2f), new Vector3(-30, 0.82f, -2.3f), new Vector3(-3f, 0.82f, 30), new Vector3(1.3f, 0.82f, -30)};
    Vector3[] carRotation = {new Vector3(0, 180, 0), new Vector3(0, 0, 0), new Vector3(0, 90, 0), new Vector3(0, -90, 0)};
    List<List<GameObject>> cars = new List<List<GameObject>>();
    public TrafficLight[] trafficLightsUI = new TrafficLight[4];

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
    public class Step
    {
        public List<CarJSON> cars;
        public List<TrafficLightJSON> trafficLights;
    }
    [System.Serializable]
    public class Values
    {
        public List<Step> values;
    }
    Dictionary<int, GameObject> carsUI = new Dictionary<int, GameObject>(); 

    Values steps; 



    private void Start() {
        for (int i = 0; i < carPositions.Length; i++)
        {
            List<GameObject> temp = new List<GameObject>();
            cars.Add(temp);
        }
        

    
        using (WebClient wc = new WebClient()){
            var json = wc.DownloadString("https://bright-agentes.us-south.cf.appdomain.cloud/");
            steps = JsonUtility.FromJson<Values>(json);

            foreach (Step step in steps.values)
            {
                // foreach (CarJSON car in step.cars)
                // {
                //     print(car.id);
                //     print(car.lane);
                // }

                foreach (TrafficLightJSON trafficLight in step.trafficLights)
                {
                    print(trafficLight.id);
                    print(trafficLight.green);
                }
            }
        }

    }

    int update=0;

    float stepSeconds =.20f;

    float waiting=0;
    
    void Update()
    {   
        waiting+= Time.deltaTime;
        if(waiting >= stepSeconds){
            waiting=0;

            Step currStep= steps.values[update];
        
            foreach (CarJSON car in currStep.cars)
            {
                if(carsUI.ContainsKey(car.id)){
                    carsUI[car.id].GetComponent<Car>().setIsMoving(car.isMoving);
                }
                else{
                    newCar(car.id,car.lane,car.destiny);
                }
            }
            foreach (TrafficLightJSON trafficLight in currStep.trafficLights)
            {   
                if(trafficLight.green){
                    trafficLightsUI[trafficLight.id].turnGreenOn();
                }
                else{
                    trafficLightsUI[trafficLight.id].turnRedOn();
                }
            
            }

            update++;

        }

        


    }

    void newCar(int id,int lane, int destination){
        Vector3 v = carRotation[lane];
        GameObject car = Instantiate(myPrefab, carPositions[lane], Quaternion.Euler(v.x, v.y, v.z));
        car.AddComponent<Car>();
        car.GetComponent<Car>().setDestination(destination);
        carsUI.Add(id,car);
    }

}