// ReactDOM.render(
//     React.DOM.h3({
//             id:"headling",
//             name:"headlingName",
//             className:"pretty",
//             htmlFor:"me",
//             style:{
//                 background:"red",
//                 color:"yellow",
//                 fontFamily:"Verdana",
//             }
//         },
//         "Hello World!"),
//     //document.getElementById("app")
// );

var TextAreaCounter = React.createClass( {

    propTypes: {
        text:React.PropTypes.string,
    },

    getDefaultProps: function() {
        return {
            text:'Please input your name!',
        };
    },

    getInitialState:function() {
        return {
            text:this.props.text,
        };
    },

    _textChange:function( ev ) {
        this.setState({
            text: ev.target.value,
        });
    },

    render: function() {
        return React.DOM.div( null, 
            React.DOM.textarea( {
                value: this.props.text,
                onChange: this._textChange,
            }),
            React.DOM.h3(null, this.props.text.length )
        );
    }
});

var MyComponent = React.createClass( {
    propTypes: {
        name:React.PropTypes.string.isRequired,
    },
    render: function() {
        return React.DOM.span(null, "What is this ?" + this.props.name );
    }
} );

var headerData = [
    "Name",
    "Age",
    "Sex"
];

var entityData = [
    [
        "likai",
        33,
        "male"
    ],
    [
        "duxiaoxia",
        33,
        "female"
    ],
    [
        "liyi",
        3,
        "male"
    ]
];
var Excel = React.createClass({
    displayName:"Excel",

    //声明属性，及其数据类型 字符串数组 arrayOf[ any ]
    propTypes:{
        headers: React.PropTypes.arrayOf( React.PropTypes.string ),
        initialData: React.PropTypes.arrayOf( React.PropTypes.any ),
    },

    //排序函数，用于点击表头进行排序
    _sort: function( e ) {
        //1.获取所选列
        var column = e.target.column;

        //2.拷贝一份表格数据
        var dataCopy=Array.from( this.props.initialData );

        //3.设置排序函数
        dataCopy.sort( function(a, b){
            return ( a[column]>b[column] ) ? (1):(-1);
        } );

        //4.将排序后的数据重设到表格中
        this.setState({
            initialData:dataCopy
        });
    },

    render:function() {
        return React.DOM.table(null, 
            React.DOM.thead( {onClick:this._sort}, 
                React.DOM.tr(null, 
                    this.props.headers.map( function(title, idx ){
                        return React.DOM.th( {key: idx}, title);
                    })
                )
            ), 

            React.DOM.tbody(null, 
                this.props.initialData.map( function(row, idx){
                    return (
                        React.DOM.tr( {key:idx}, 
                        row.map( function(cell, idx){
                            return React.DOM.td( {key:idx}, cell );
                        } )
                        )
                    );
                } )
            )
        )
    }
});

ReactDOM.render(
    // React.createElement( 
    //     TextAreaCounter,
    //     {
    //         text:"Du Xiaoxia" 
    //     }
    // ),

    //React.createElement( MyComponent, {name: "xia"} ,

    React.createElement( Excel, {
        headers: headerData,
        initialData: entityData,
    }),

    document.getElementById("app")
)