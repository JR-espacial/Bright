using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class main : MonoBehaviour
{
    public GameObject myPrefab;
    Vector3[] carPositions = {new Vector3(30, 2.5f, 2), new Vector3(-30, 2.5f, -2), new Vector3(-2, 2.5f, 28), new Vector3(2, 2.5f, -28)};
    Vector3[] carRotation = {new Vector3(0, 180, 0), new Vector3(0, 0, 0), new Vector3(0, 90, 0), new Vector3(0, -90, 0)};
    List<List<GameObject>> cars = new List<List<GameObject>>();

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
    }
    void Update()
    {   
        //to stop car movement
        //cars[0][0].GetComponent<Car>().setIsMoving(false);
    }

    void newCar(int lane, int destination){
        Vector3 v = carRotation[lane];
        GameObject car = Instantiate(myPrefab, carPositions[lane], Quaternion.Euler(v.x, v.y, v.z));
        car.AddComponent<Car>();
        car.GetComponent<Car>().setDestination(destination);
        cars[lane].Add(car);
    }

}
