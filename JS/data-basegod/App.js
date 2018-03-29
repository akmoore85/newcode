import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

export default class App extends React.Component {
    render() {
        return ( <
            View style = { styles.container } >
            <
            Text > Open up App.js to start working on your app! < /Text> <
            Text > Testing Testing where will this show up < /Text>  <
            Image source = { require('https://www.hotleathers.com/patch-skeleton-peace-sign-ppa9098') }
            /> <
            /View >
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
});