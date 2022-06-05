import { Injectable } from '@angular/core';

@Injectable()

export class LocationService {
    private time = ''
    private referencePoint = ''
    private lineName = '';
    private referencePointId = '';
    private lineId = '';

    locateLine(lineid: string, referencePointId: string, lineName: string, referencePointName: string){
        //Todo fazer request do tempo com o id do ponto e buscar no resultado, com o id da linha, o tempo que falta - formato 

        //Todo - pegar do tempo os minutos
        let horas = '10';

        //Todo - pegar do tempo os segundos
        let minutos = '30';

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
    
}