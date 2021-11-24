using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class main : MonoBehaviour
{
    public GameObject myPrefab;
    Vector3[] carPositions = {new Vector3(30, 2.5f, 2), new Vector3(-30, 2.5f, -2), new Vector3(-2, 2.5f, 28), new Vector3(2, 2.5f, -28)};
    Vector3[] carRotation = {new Vector3(0, 180, 0), new Vector3(0, 0, 0), new Vector3(0, 90, 0), new Vector3(0, -90, 0)};

    private void Start() {
        newCar(0);
        newCar(1);
        newCar(2);
        newCar(3);
    }
    void Update()
    {
        
    }

    void newCar(int lane){
        Vector3 v = carRotation[lane];
        GameObject car = Instantiate(myPrefab, carPositions[lane], Quaternion.Euler(v.x, v.y, v.z));
        car.AddComponent<Car>();
    }

    
}
