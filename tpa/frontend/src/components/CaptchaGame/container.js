import React, { Component } from "react";
import PropTypes from "prop-types";
import CaptchaGame from "./presenter";

class Container extends Component {
  state = {
    answer : "",
    inputValue : "",
    time : 1000,
    isTimer : false,
    score : 1,
  };
  
  static propTypes = {
   
  };
  componentWillReceiveProps = nextProps => {
    
  }
  generateCaptcha() {
    var captcha = document.getElementById("captcha");
    var text = this.generateRandomString(6); // 6글자 무작위 문자열 생성
    this.setState({
      answer : text,
    })
    captcha.innerHTML = "";
    var color = this.getRandomColor();
    var cColor = this.getComplementaryColor(color);
    for (var i = 0; i < text.length; i++) {
      var span = document.createElement("span");
      span.className = "letter";
      span.style.display = "inline-block";
      span.style.zIndex = "2";
      span.style.color = color;
      span.style.margin = "0 10px";
      span.style.position = "relative";
      span.style.fontWeight = "600px";
      span.style.transformOrigin = "bottom center";
      span.style.fontFamily = this.getRandomFont(); // 무작위 폰트 적용
      span.style.fontSize =  this.getRandomInt(40, 60) + "px"
      span.style.transform = "rotate(" + this.getRandomInt(-13, 13) + "deg)"; // 무작위로 -30도에서 30도 사이에서 기울기 적용
      span.textContent = text[i];
      captcha.appendChild(span);
    }
    this.drawLineOverText(color,cColor);
  }
  getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  
  getComplementaryColor(hexcolor){
    // Convert hex to RGB
    var r = parseInt(hexcolor.substr(1,2),16);
    var g = parseInt(hexcolor.substr(3,2),16);
    var b = parseInt(hexcolor.substr(5,2),16);

    // Get complementary color
    r = 255 - r;
    g = 255 - g;
    b = 255 - b;

    // Convert RGB to hex
    r = r.toString(16);
    g = g.toString(16);
    b = b.toString(16);

    // Return complementary color
    return "#" + this.padZero(r) + this.padZero(g) + this.padZero(b);
  }
  padZero(str) {
    var len = 2;
    var zeros = new Array(len).join('0');
    return (zeros + str).slice(-len);
  }
  drawLineOverText(color,cColor) {
    var canvas = document.getElementById('overlay');
    var ctx = canvas.getContext('2d');
    var captchaContainer = document.getElementById("container");
  
    // 캡챠 컨테이너와 같은 크기로 canvas를 설정합니다.
    canvas.width = captchaContainer.offsetWidth;
    canvas.height = captchaContainer.offsetHeight;
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    // 분홍색 배경을 칠합니다.
    ctx.fillStyle = cColor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // 흰색 선을 랜덤으로 여러 개 그립니다.
    for (let i = 0; i < 80; i++) { // 선의 수를 원하는 만큼 조절할 수 있습니다.
      let x1, y1, x2, y2, lineLength;
      do {
        x1 = Math.random() * canvas.width;
        y1 = Math.random() * canvas.height;
        x2 = Math.random() * canvas.width;
        y2 = Math.random() * canvas.height;
        lineLength = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
      } while (lineLength > 10)  // 선의 길이가 3px보다 큰 경우, 새 좌표를 재설정합니다.

      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = color;
      ctx.lineWidth = 1; // 선의 두께를 설정합니다. 필요에 따라 변경할 수 있습니다.
      ctx.stroke();
    }
    // 시작점과 끝점을 무작위로 설정하여 선을 그립니다.
    var x1 = this.getRandomInt(0, canvas.width / 4);
    var y1 = this.getRandomInt(canvas.height / 4, canvas.height / 2);
    var x2 = this.getRandomInt(canvas.width /4 * 3, canvas.width);
    var y2 = this.getRandomInt(canvas.height / 2, canvas.height / 4 * 3);
    
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.strokeStyle = '#FFFFFF'; // 선의 색을 설정합니다. 필요에 따라 변경할 수 있습니다.
    ctx.lineWidth = 2; // 선의 두께를 설정합니다. 필요에 따라 변경할 수 있습니다.
    ctx.stroke();
  }
  generateRandomString(length) {
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (var i = 0; i < length; i++)
      text += possible.charAt(Math.floor(Math.random() * possible.length));
    return text;
  }
  
  getRandomFont() {
    var fonts = ["font1", "font2", "font3", "font4", "font5", "font6"]; // 사용할 폰트 목록
    return fonts[Math.floor(Math.random() * fonts.length)];
  }
  
  getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  handleChange = (event) => {
    const newValue = event.target.value.toUpperCase();
    if (this.isValidEnglishAlphabet(newValue)) {
      this.setState({ inputValue: newValue });
    }
  };

  handleKeyDown = (event) => {
    if (event.key === "Enter") {
      const { inputValue, answer } = this.state;
      if (inputValue === answer) {
        this.setState({
          score : this.state.score + 1,
          time : this.state.time + 200
        })
        this.generateCaptcha();
      }
      this.setState({
        inputValue : "",
      })
    }
    if (event.key === "Backspace") {
      return;
    }

    const inputChar = event.key;
    if (!this.isValidEnglishAlphabet(inputChar)) {
      event.preventDefault();
    }
  };
  handleFocus = () => {
    this.startTimer();
  }
  startTimer = () => {
    if(!this.state.isTimer){
      this.timerInterval = setInterval(this.updateElapsedTime, 10);
      this.setState({isTimer: true});
    }
  }
  updateElapsedTime = () => {
  if(this.state.time>=0){
    this.setState({ time : this.state.time - 1});
  }
  else{
    clearInterval(this.timerInterval);
    this.setState({ isTimer: false });
    alert("[게임 오버]\n 최종 LV "+ this.state.score+" 단계");
    window.location = "/physical"
  }
  };
  isValidEnglishAlphabet = (text) => {
    const englishAlphabetRegex = /^[a-zA-Z]*$/; // 여러 문자를 검사할 수 있도록 변경
    return englishAlphabetRegex.test(text);
  };
  reload = () => {
    this.generateCaptcha();
  }
  componentDidMount() {
    document.title = "캡챠 피지컬 연습";
    this.generateCaptcha();
  };
  render() {
    return (
      <>
      <CaptchaGame handleFocus={this.handleFocus} reload={this.reload} handleChange={this.handleChange} handleKeyDown={this.handleKeyDown} {...this.state}/>
      </>
    );
  }
}

export default Container;