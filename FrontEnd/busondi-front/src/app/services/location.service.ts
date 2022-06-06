import { Injectable } from '@angular/core';

@Injectable()

export class LocationService {
    private time = ''
    private referencePoint = ''
    private lineName = '';
    private referencePointId = '';
    private lineId = '';
    private lineRouteId = '';
    private lineRouteName = '';


    randomIntFromInterval(min : number, max: number) { // min and max included 
        return Math.floor(Math.random() * (max - min + 1) + min)
    }

    locateLine(lineid: string, referencePointId: string, lineName: string, referencePointName: string){
        //Todo fazer request do tempo com o id do ponto e buscar no resultado, com o id da linha, o tempo que falta - formato 
        
        let now = new Date();
        //Todo - pegar do tempo os minutos
        let horas = now.getHours();;

        //Todo - pegar do tempo os segundos
        let minutos = now.getMinutes() + this.randomIntFromInterval(1,5);
        
        if(minutos > 60){
            minutos = 59;
        }

        this.referencePoint = referencePointName;
        this.lineName = lineName;

        this.time = horas + ' horas e ' + minutos + ' minutos';
    }

    updateLine(referencePointId: string, referencePointName: string){
        this.locateLine(this.lineId, referencePointId, this.lineName, referencePointName);
    }

    getDeparture(){
        return this.referencePoint;
    }

    getLine(){
        return this.lineName;
    }

    getTime(){
        return this.time;
    }

    locateLineOnRoute(lineId: string, lineName: string){
        console.log(lineName);
        this.lineRouteId = lineId;
        this.lineRouteName = lineName
    }

    getLineRoute(){
        return this.lineRouteName;
    }
    
}