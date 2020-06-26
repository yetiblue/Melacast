<template>
  <div>
        <form method="POST" name = "postform" action='http://127.0.0.1:8000/api/v1/heroes/?format=json' onSubmit="postUsers()">
            <input type="text" name = "name" id="name">
            <input type="text" name = "alias" id = "alias">
            <input type="submit" name="submit">
        </form>
    </div>
</template>

<script>

export default {
   
};
</script>
<style >

</style>

 