    var canvas, ctx, bTrackCoords = false,
        prevX = 0,
        currX = 0,
        prevY = 0,
        currY = 0,
        dot_flag = false;
        sokgraph_x = [];
        sokgraph_y = [];

    var lineColor = "black",
        lineWidth = 2;

    $(function() {
        canvas = document.getElementById('can');
        ctx = canvas.getContext("2d");
        w = canvas.width;
        h = canvas.height;

        canvas.addEventListener("mousemove", function(e) {
            findxy('move', e)
        }, false);
        canvas.addEventListener("mousedown", function(e) {
            findxy('down', e)
        }, false);
        canvas.addEventListener("mouseup", function(e) {
            findxy('up', e)
        }, false);
        canvas.addEventListener("mouseout", function(e) {
            findxy('out', e)
        }, false);
    });


    function draw()
    {
        ctx.beginPath();
        ctx.moveTo(prevX, prevY);
        ctx.lineTo(currX, currY);
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = lineWidth;
        ctx.stroke();
        ctx.closePath();
    }

    function findxy(res, e)
    {
        if (res == 'down')
        {
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
            prevX = currX;
            prevY = currY;

            //when clicking on a point in the canvas, the x value gets pushed here, but the y value gets pushed here and
            //somewhere else
//            sokgraph_x.push(currX);
//            sokgraph_y.push(currY);

            //the user has clicked, so we should start tracking their mouse movements
            bTrackCoords = true;
            dot_flag = true;
            if (dot_flag)
            {
                ctx.beginPath();
                ctx.fillStyle = lineColor;
                ctx.fillRect(currX, currY, 2, 2);
                ctx.closePath();
                dot_flag = false;
            }
        }
        if (res == 'up' || res == "out")
        {
            if(bTrackCoords)
            {
                alert("X values: " + sokgraph_x);
                alert("Y values: " + sokgraph_y);
                alert("X values: " + sokgraph_x);

                alert("X length: " + sokgraph_x.length);
                alert("Y length: " + sokgraph_y.length);

                //get the arrays ready to store the next sokgraph and stop tracking their
                //coordinates until they click again
                sokgraph_x = [];
                sokgraph_y = [];
                bTrackCoords = false;

            }
            erase();
        }
        if (res == 'move')
        {
            if (bTrackCoords)
            {
                prevX = currX;
                prevY = currY;
                currX = e.clientX - canvas.offsetLeft;
                currY = e.clientY - canvas.offsetTop;
                sokgraph_x.push(currX);
                sokgraph_y.push(currY);
                draw();
            }
        }

        function erase()
        {
            ctx.clearRect(0, 0, w, h);

            //as is, this throws a TypeError because that element does not exist. If it gets added, we should uncomment this
            //document.getElementById("canvasimg").style.display = "none";

        }
    }