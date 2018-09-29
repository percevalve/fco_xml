<template>
<div>
    <!-- <img class="background" src="https://i.giphy.com/media/U3qYN8S0j3bpK/source.gif"> -->

  <div class="container">
    <p ref="discover"></p>  
    <!-- <h1>Portraits of ministers</h1> -->
    <!-- <iframe style="width: 80vw; height: 50vh; border: none;" src="https://query.wikidata.org/embed.html#%23%20Wikidata%20entries%20for%20British%20ambassadors%20and%20high%20commissioners%0A%23%20all%20people%20who%20held%20at%20least%20one%20such%20position%0A%23%20one%20line%20per%20position%20held%20%28so%20many%20people%20appear%20repeatedly%29%0A%23%20start%2Fend%20dates%20for%20that%20particular%20position%0A%0Aselect%20%3Fperson%20%3FpersonLabel%20%3FpositionLabel%20%3Fstartyear%20%3Fendyear%20%3Fimage%20where%0A%7B%0A%20%20%7B%20%3Fposition%20wdt%3AP31%20wd%3AQ18115939%20.%20%7D%20union%20%7B%20%3Fposition%20wdt%3AP31%20wd%3AQ56760832%20%7D%20.%20%23%20position%20is%20UK%20ambassador%20or%20high%20commissioner%0A%20%20%20%20%0A%20%20%20%20%3Fperson%20p%3AP39%20%3FpositionStatement%20.%20%3FpositionStatement%20ps%3AP39%20%3Fposition%20.%20%23%20find%20positions%20they%20held%0A%20%20optional%20%7B%20%3Fperson%20wdt%3AP18%20%3Fimage%20.%20%7D%20.%20%20%0A%20%20optional%20%7B%20%3FpositionStatement%20pq%3AP580%20%3Fstart%20.%20bind%28year%28%3Fstart%29%20as%20%3Fstartyear%29%20%7D%20%23%20id%20start%20year%0A%20%20%20%20optional%20%7B%20%3FpositionStatement%20pq%3AP582%20%3Fend%20.%20bind%28year%28%3Fend%29%20as%20%3Fendyear%29%20%7D%20%23%20id%20end%20year%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%20%20%23defaultView%3AImageGrid%0A%7D" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups" ></iframe> -->

    <hr>

    <h1>Search for a <b>Diplomat</b> | <small>Discover <b>Insights</b></small></h1>

    <p>Type bellow to get started</p>

      <v-select v-model="person" label="personLabel" :options="options" @search="onSearch"></v-select>
    
    <hr>

    <!-- {{person}} -->
    <div v-if="person" style="text-align: left">
      <img width="300" v-if="person.img_url" :src="person.img_url" style="float: left; margin-right: 25px">
      <p v-else>Image not found</p>

      <div class="deets" style="float: right">
        <h2><a :href="person.person" target="_blank">{{person.personLabel}}</a></h2>


        <!-- <p><b>Born:</b> {{person.startyear}}<br> -->
        <!-- <b>Died:</b> {{person.endyear}}</p> -->
        
        <p v-if="person.positionLabels"><b>Ambassadorial positions:</b></p>
        <hr>

        <div v-for="position in person.positionLabels" v-if="person.positionLabels && person.positionLabels.length">
          - {{position.positionLabel.value}} ({{position.startyear.value}} - {{position.endyear.value}})
        </div>

        {{person.positionLabel}}
        
        <p v-if="person.otherPositions && person.otherPositions.length"><b>Other positions held:</b>
          <hr>
        <div v-for="otherposition in person.otherPositions">
          >> {{otherposition.label.value}}
          ({{otherposition.startyear.value}} -
          {{otherposition.endyear.value}} )
        </div>
        
      </div>

    </div>


    <form>
      
    </form>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import Typed from 'typed'

// http://localhost:8080/wikidata/person/picker/<keyword>

export default {
  name: 'HelloWorld',
  mounted () {
    // alert(this.$refs.discover)
    var typed = new Typed(this.$refs.discover, {
      strings: ["First sentence.", "Second sentence."],
      typeSpeed: 30
    })
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      options: [],
      selected: null,
      person: {}
    }
  },
  methods: {
    onSearch (search, loading) {
      loading(true)
      let url = "http://localhost:8000/wikidata/person/picker/" + search
      axios.get(url).then(res => {
        let results = res.data
        console.log(results)
        this.options = results
        loading(false)
      })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.background {
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
  opacity: 0.1;
  width: 100%;
}

.container {
  width: 80%;
  margin: 20px auto;
}


h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
