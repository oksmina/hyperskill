async function findUserById(id) {
  return new Promise((resolve, reject) => {
    if (users[id]) {
      setTimeout(() => resolve(users[id]), 1000);
    }
      setTimeout(() => reject('No user with this id'), 1000);
  });
}

async function handleResult(number) {
  try {
    const resultOfThePromisse = await findUserById(number);
    console.log(resultOfThePromisse);
  } catch(err) {
    console.log(err);
  }
}
