using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TrafficLight : MonoBehaviour
{

    private Material materialTrafficLight;
    private readonly int _greenOn = Shader.PropertyToID("_greenOn");
    private readonly int _yellowOn = Shader.PropertyToID("_yellowOn");
    private readonly int _redOn = Shader.PropertyToID("_redOn");


    // Start is called before the first frame update
    void Start()
    {
        materialTrafficLight = gameObject.GetComponent<MeshRenderer>().material;
    }

    // Update is called once per frame
    void Update()
    {
    }

    public void turnGreenOn() {
        materialTrafficLight.SetFloat(_greenOn, 1.0f);
        materialTrafficLight.SetFloat(_yellowOn, 0.0f);
        materialTrafficLight.SetFloat(_redOn, 0.0f);
    }

    public void turnYellowOn() {
        materialTrafficLight.SetFloat(_greenOn, 0.0f);
        materialTrafficLight.SetFloat(_yellowOn, 1.0f);
        materialTrafficLight.SetFloat(_redOn, 0.0f);
    }

    public void turnRedOn() {
        materialTrafficLight.SetFloat(_greenOn, 0.0f);
        materialTrafficLight.SetFloat(_yellowOn, 0.0f);
        materialTrafficLight.SetFloat(_redOn, 1.0f);
    }
}
